from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('categories/', include('product.urls')),
    path('search/', include('product.urls')),
    path('basket/', include('basket.urls'))
]