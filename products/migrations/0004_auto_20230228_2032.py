# Generated by Django 3.2.18 on 2023-02-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230228_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
