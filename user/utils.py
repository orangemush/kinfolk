import jwt
import json

from django.http       import JsonResponse

from local_settings    import SECRERT_KEY, ALGORITHM
from .models           import Account

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if not 'Authorization' in request.headers:
            return JsonResponse({"message": "INVALID_LOGIN"}, status = 401)
        token = request.headers.get('Authorization', None)

        try:
            user_token   = jwt.decode(token, SECRERT_KEY, algorithm = ALGORITHM)
            user         = Account.objects.get(Qemail = user_token)
            request.user = user
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status = 400)

        except Account.DoesNotExist:
            return JsonResponse({"message": "Invalid_USER"}, status = 400)
        return func(self, request, *args, **kwargs)
    return wrapper


