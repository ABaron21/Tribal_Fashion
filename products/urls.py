from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product_details/<int:product_id>', views.product_details,
         name='product_details'),
    path('add_product/<int:retailer_id>', views.add_product,
         name='add_product'),
    path('update_product/<int:retailer_id>',
         views.update_product, name='update_product')
]
