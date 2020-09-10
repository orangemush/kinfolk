from django.db   import models

from user.models    import Account 
from product.models import (
    ShopProduct,
    CategoryProduct
)

class Basket(models.Model):
    product     = models.CharField(max_length = 512, null = True)
    account     = models.ForeignKey(Account, on_delete = models.CASCADE, null = True)

class Coupon(models.Model):
    coupon_code = models.CharField(max_length = 32)
    discount    = models.DecimalField(max_digits = 2, decimal_places = 2)
    basket      = models.ForeignKey(Basket, on_delete = models.CASCADE)