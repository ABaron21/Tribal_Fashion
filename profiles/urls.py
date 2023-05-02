from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_setup', views.profile_setup, name='profile_setup'),
    path('retailer_request', views.retailer_request, name='retailer_request'),
    path('order_view/<order_number>', views.order_view, name='order_view'),
    path('order_cancel/<order_number>', views.order_cancel, name='order_cancel'),
]
