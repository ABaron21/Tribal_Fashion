from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.retailer_dashboard, name='retailer_dashboard'),
    path('premium_success', views.premium_success, name='premium_success'),
    path('premium_cancelation', views.premium_cancelation, name='premium_cancelation'),
]
