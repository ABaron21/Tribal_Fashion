from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_success/<order_number>&<save_info>', views.order_success, name='order_success'),
]
