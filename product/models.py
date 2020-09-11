from django.db import models

class Category(models.Model):
    categories_name = models.CharField(max_length = 512)

    class Meta:
        db_table = 'categories'

class ShopProduct(models.Model):
    product_type            = models.TextField(max_length = 32)
    outer_tag               = models.TextField(max_length = 32)
    price                   = models.DecimalField(max_digits = 6, decimal_places = 0)
    outer_image_url         = models.TextField(max_length = 1024)
    inner_tag               = models.TextField(max_length = 32)
    inner_imgae_url         = models.TextField(max_length = 1024)
    inner_description       = models.TextField(max_length = 1024)
    inner_details           = models.TextField(max_length = 1024)
    inner_shipping_handling = models.TextField(max_length = 1024)
  
    class Meta:
        db_table = 'shop_products'

class CategoryProduct(models.Model):
    image_url       = models.TextField(max_length = 1024)
    tag             = models.TextField(max_length = 32)
    title           = models.TextField(max_length = 32)
    description     = models.TextField(max_length = 1024)
    published_data  = models.TextField(max_length = 32)
    category        = models.ForeignKey('Category', on_delete = models.CASCADE)

    class Meta:
        db_table = 'category_products'