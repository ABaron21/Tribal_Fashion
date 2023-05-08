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
    path('remove_tribal_product/<int:product_id>', views.remove_tribal_product,
         name='remove_tribal_product'),
    path('order_cancellations', views.order_cancel_requests,
         name='order_cancel_requests'),
    path('order_cancel_review/<order_number>', views.order_cancellation,
         name='order_cancel_review')
]
