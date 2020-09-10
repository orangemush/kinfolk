import os
import django
import csv
import sys
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kinfolk.settings")
django.setup()

from product.models import Category, CategoryProduct, ShopProduct

CSV_PATH_PRODUCTS = ['./kinfolk_design.csv', './kinfolk_fashion.csv', './kinfolk_shop_artprints.csv', './kinfolk_shop_book.csv', './kinfolk_shop_magazine.csv']

with open(CSV_PATH_PRODUCTS[0]) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        CategoryProduct.objects.create(
            category       = Category.objects.get(categories_name = row[0]),
            image_url      = row[1],
            tag            = row[2],
            title          = row[3],
            description    = row[4],
            published_data = row[5]
        )

with open(CSV_PATH_PRODUCTS[1]) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        CategoryProduct.objects.create(
            category       = Category.objects.get(categories_name = row[0]),
            image_url      = row[1],
            tag            = row[2],
            title          = row[3],
            description    = row[4],
            published_data = row[5]
        )

with open(CSV_PATH_PRODUCTS[2]) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        ShopProduct.objects.create(
            product_type            = row[0],
            outer_tag               = row[1],
            price                   = row[2],
            outer_image_url         = row[3],
            inner_tag               = row[4],
            inner_imgae_url         = row[5],
            inner_description       = row[6],
            inner_details           = row[7],
            inner_shipping_handling = row[8]
        )
with open(CSV_PATH_PRODUCTS[3]) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        ShopProduct.objects.create(
            product_type            = row[0],
            outer_tag               = row[1],
            price                   = row[2],
            outer_image_url         = row[3],
            inner_tag               = row[4],
            inner_imgae_url         = row[5],
            inner_description       = row[6],
            inner_details           = row[7],
            inner_shipping_handling = row[8]
        )
with open(CSV_PATH_PRODUCTS[4]) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        ShopProduct.objects.create(
            product_type            = row[0],
            outer_tag               = row[1],
            price                   = row[2],
            outer_image_url         = row[3],
            inner_tag               = row[4],
            inner_imgae_url         = row[5],
            inner_description       = row[6],
            inner_details           = row[7],
            inner_shipping_handling = row[8]
        )