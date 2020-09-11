from django.urls import path
from .views      import BasketView

urlpatterns = [
    path('product', BasketView.as_view())
]