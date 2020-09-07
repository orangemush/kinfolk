import json
import bcrypt
import jwt

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.db.models       import Q

from .validator      import password_validate
from local_settings import SECRET_KEY, ALGORITHM
from user.models    import Account

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            password_validate(password)

            if Account.objects.filter(email = email).exists():
                return JsonResponse({"message": "DUPLICATED_USER"}, status = 400)

            encoded_password = password.encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            
            Account(
                email     = email,
                password  = hashed_password.decode('utf-8'),
                user_name = email[:email.index('@')]
            ).save()
        
        except ValidationError:
            return JsonResponse({"message": "INVALID_PASSWORD_OR_EMAIL"}, status = 400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)

        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)

        except json.JSONDecodeError:
            return JsonResponse({"message": "WORNG_JSON_FORM"}, status = 400)
        return JsonResponse({"message": "Success"}, status = 200)
    
    def get(self, request):
        return JsonResponse( {"message": list(Account.objects.values())}, status = 200 )

    def delete(self, request):
        Account.objects.all().delete()
        return JsonResponse({"message": "deleted all"}, status = 200)

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email     = data['email']
            password  = data['password']

            if Account.objects.filter(Q(email = email) | Q(user_name = email)).exists():
                account = Account.objects.get(Q(email = email) | Q(user_name = email))
                pwd     = account.password

                if bcrypt.checkpw(password.encode('utf-8'), pwd.encode('utf-8')):
                    token = jwt.encode({'email': data['email']}, SECRET_KEY, algorithm = ALGORITHM)
                    return JsonResponse({"token": token.decode('utf-8')}, status = 200)

                return JsonResponse({"message": "DUPLICATED_USER"}, status = 400)
            return JsonResponse({"message": "INVALID_USER"}, status = 400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)

        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"message": "JSONDecodeError"}, status = 400)