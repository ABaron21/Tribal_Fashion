from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('retailer-request', views.retailer_request, name='retailer_request'),
]
