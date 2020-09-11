from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_name', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.TextField(max_length=32)),
                ('outer_tag', models.TextField(max_length=32)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('outer_image_url', models.TextField(max_length=1024)),
                ('inner_tag', models.TextField(max_length=32)),
                ('inner_imgae_url', models.TextField(max_length=1024)),
                ('inner_description', models.TextField(max_length=1024)),
                ('inner_details', models.TextField(max_length=1024)),
                ('inner_shipping_handling', models.TextField(max_length=1024)),
            ],
            options={
                'db_table': 'shop_products',
            },
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField(max_length=1024)),
                ('tag', models.TextField(max_length=32)),
                ('title', models.TextField(max_length=32)),
                ('description', models.TextField(max_length=1024)),
                ('published_data', models.TextField(max_length=32)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'category_products',
            },
        ),
    ]
