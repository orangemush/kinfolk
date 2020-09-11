import json 

from django.views           import View
from django.http            import JsonResponse
from django.db.models       import Q
from django.core.paginator  import Paginator

from product.models         import Category, ShopProduct, CategoryProduct

class DesignView(View):
    def get(self, request):
        design_all = list(CategoryProduct.objects.filter(category_id = 1).values())
        return JsonResponse({'Design': design_all}, status = 200)

class FashionView(View):
    def get(self, request):
        fashion_all = list(CategoryProduct.objects.filter(category_id = 2).values())
        return JsonResponse({'Fashion': fashion_all}, status = 200)

class ShopView(View):
    def get(self, request):
        shop_all = list(ShopProduct.objects.all().values())
        return JsonResponse({'Products': shop_all}, status = 200)

class ShopBookView(View):
    def get(self, request):
        book_all = list(ShopProduct.objects.filter(product_type = 'Books').values())
        return JsonResponse({'Books': book_all}, status = 200)

class ShopArtprintView(View):
    def get(self, request):
        artprint_all = list(ShopProduct.objects.filter(product_type = 'Art Prints').values())
        return JsonResponse({'Artprints': artprint_all}, status = 200)

class ShopMagazineView(View):
    def get(self, request):
        magazine_all = list(ShopProduct.objects.filter(product_type = 'Magazine').values())
        return JsonResponse({'Magazines': magazine_all}, status = 200)

class ProductDetail(View):
    def get(self, request):
        item_id = request.GET.get("item", None)
        item_detail = list(ShopProduct.objects.filter(id  = item_id).values())
        if item_detail == []:
            return JsonResponse({'Massage': 'There is no applicable product'}, status = 400)
        return JsonResponse({'Detail': item_detail}, status = 200)

class SearchView(View):
    def get(self, request, item):
        results = []
        search_shop = list(ShopProduct.objects.filter(
            Q(outer_tag__icontains = item) | 
            Q(inner_description__icontains = item) | 
            Q(inner_details__icontains = item)
            ).values()
        )
        search_category = list(CategoryProduct.objects.filter(
            Q(title__icontains = item) | 
            Q(description__icontains = item) | 
            Q(tag__icontains = item)
            ).values()
        )
        results.append(search_shop)
        results.append(search_category)

        if results[0] == []:
            return JsonResponse({'Massage': 'No results found'}, status = 400)
        return JsonResponse({'search_results': results}, status = 200)