# Generated by Django 4.0.2 on 2022-02-23 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_customer_product_order'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
