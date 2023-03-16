from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.retailer_dashboard, name='retailer_dashboard'),
]
