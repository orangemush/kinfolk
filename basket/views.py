import json
from ast              import literal_eval
from django.views     import View
from django.http      import JsonResponse

from local_settings   import SECRET_KEY, ALGORITHM

from basket.models    import Basket
from user.models      import Account
from product.models   import (
    ShopProduct,
    CategoryProduct
) 

class BasketView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            product_id    = data['product_id']
            quantity      = data['quantity']
            account_email = data['account_email']
            account       = Account.objects.get(email = account_email)

            if len(Basket.objects.filter(account = account)) == 0:
                Basket.objects.create (
                    product = {product_id[i]: quantity[i] for i in range(len(product_id))},
                    account = account
                )

            else:
                user_basket = Basket.objects.get(account = account) 
                product     = literal_eval(user_basket.product)

                for i in range(len(product_id)):
                    product[product_id[i]] = quantity[i]
                user_basket.product = str(product)
                user_basket.save()
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)
        except Basket.DoesNotExist:
            return JsonResponse({"message": "DoesNotExist Basket"}, status = 400)
        except Account.DoesNotExist:
            return JsonResponse({"message": "DoesNotExist Account"}, status = 400)
        return JsonResponse({"message": "UPDATED"}, status = 200)

    def get(self, request):
        try:
            account_email   = request.headers['Authorization']
            account         = Account.objects.get(email = account_email)
            user_basket     = Basket.objects.get(account = account)
            products        = literal_eval(user_basket.product)

            product_list = []
            product_info = {"products": product_list}
            for product_id in list(products.keys()):
                product     = ShopProduct.objects.get(id = product_id)
                quantity    = products[product_id]

                product_list.append(
                    {
                        "product_tag"    : product.outer_tag,
                        "outer_image_url": product.outer_image_url,
                        "product_price"  : product.price,
                        "quantity"       : quantity
                    }
                )
            return JsonResponse(product_info, status = 200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)
        except Account.DoesNotExist:
            return JsonResponse({"message": "No_Account_Exist"}, status = 400)

    def delete(self, request):
        try:
            data          = json.loads(request.body)
            product_id    = data['product_id']
            account_email = data['account_email']
            account       = Account.objects.get(email = account_email)
            user_basket   = Basket.objects.get(account = account)
            product       = literal_eval(user_basket.product)

            for i in product_id:
                del product[i]
            user_basket.product = str(product)
            user_basket.save()
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)
        except Account.DoesNotExist:
            return JsonResponse({"message":"No Account Exist"}, status = 400)
        return JsonResponse({"message": "DELETED"}, status = 200)

