from datetime   import date

from django.db  import models

from .validator import password_validate


class Account(models.Model):
    email        = models.EmailField(max_length = 64)
    password     = models.CharField(max_length = 256, validators = [password_validate])
    user_name    = models.CharField(max_length = 32, null = True)
    display_name = models.CharField(max_length = 32, null = True)
    real_name    = models.CharField(max_length = 32, null = True)
    kakao_id     = models.CharField(max_length = 64, null = True)

class ShippingAddress(models.Model):
    recipient      = models.CharField(max_length = 64)
    company_name   = models.CharField(max_length = 64, null = True)
    country_region = models.CharField(max_length =  64)
    street_address = models.CharField(max_length = 512)
    post_code      = models.IntegerField()
    town_city      = models.CharField(max_length = 32)
    account        = models.ForeignKey(Account, on_delete = models.CASCADE)

class BillingAddress(models.Model):
    recipient      = models.CharField(max_length = 64)
    company_name   = models.CharField(max_length = 64, null = True)
    country_region = models.CharField(max_length =  64)
    street_address = models.CharField(max_length = 512)
    post_code      = models.IntegerField()
    town_city      = models.CharField(max_length = 32)
    account        = models.ForeignKey(Account, on_delete = models.CASCADE)