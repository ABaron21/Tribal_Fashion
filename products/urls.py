from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add_product/<int:retailer_id>', views.add_product,
         name='add_product')
]
