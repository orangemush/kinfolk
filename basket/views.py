import json

from django.views     import View
from django.http      import JsonResponse

from local_settings   import SECRET_KEY, ALGORITHM
from basket.models    import Basket
from product.models   import (
    ShopProduct,
    CategoryProduct
) 


class BasketView(View):
    def post(self, request):
        pass
    
    def get(self, request):
        pass

    def put(self, request):
        try:
            data        = json.loads(request.body)
            quantity    = data['quantity']
            product_id  = data['id']

            product     = ShopProduct.objects.get(id = product_id)
            
            Basket.objects.create(
                shop_product = product,
                quantity     = quantity
            )

            account_id  = data['account_id']

            basket = Basket.objects.get(account = account_id)
            if len(basket.objects.all()) == 0:
                Basket.objects.create (
                product = {product_id: quantity},
                account = account_id
            )

            else:
                basket.objects.product[product_id] = quantity
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)
        return JsonResponse({"message": "UPDATED"}, status = 200)

    def delete(self, request):
        try:
            data        = json.loads(request.body)
            product_id  = data['id']
            account_id  = data['account_id']

            Basket.objects.get(account = account_id).delete()
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status = 400)
        return JsonResponse({"message": "DELETED"}, status = 200)

