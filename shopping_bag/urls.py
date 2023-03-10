from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_bag'),
    path('add_to_bag/<int:product_id>', views.add_to_bag, name='add_to_bag'),
    path('adjust_quantity/<product_id>', views.adjust_quantity,
         name='adjust_quantity'),
    path('remove_item/<product_id>', views.remove_item,
         name='remove_item'),
]
