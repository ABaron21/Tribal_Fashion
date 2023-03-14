from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_setup', views.profile_setup, name='profile_setup'),
    path('retailer-request', views.retailer_request, name='retailer_request'),
]
