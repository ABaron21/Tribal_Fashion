from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_dashboard, name='management_dashboard'),
    path('retailer_requests', views.retailer_requests,
         name='retailer_requests'),
    path('approve_retailer/<int:request_user_id>', views.approve_retailer,
         name='approve_retailer'),
    path('premium_cancel_requests', views.premium_cancel_requests,
         name='premium_cancel_requests'),
    path('approve_cancelation/<int:retailer_id>', views.approve_cancelation,
         name='approve_cancelation'),
]
