from django.urls import path, include

from .views import (
    DesignView, 
    FashionView,
    ShopView,
    ShopBookView,
    ShopArtprintView,
    ShopMagazineView,
    ProductDetail,
    SearchView
)

urlpatterns = [
    path('designs', DesignView.as_view()),
    path('fashions', FashionView.as_view()),
    path('shop', ShopView.as_view()),
    path('shop/books', ShopBookView.as_view()),
    path('shop/art-prints', ShopArtprintView.as_view()),
    path('shop/magazines', ShopMagazineView.as_view()),
    path('shop/products', ProductDetail.as_view()),
    path('<str:item>', SearchView.as_view()),
]