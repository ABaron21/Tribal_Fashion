from django.shortcuts import (render, get_list_or_404, get_object_or_404,
                              redirect, reverse)
from profiles.models import UserAccount, RetailAccount
from products.models import Product

# Create your views here.


def retailer_dashboard(request):
    user = get_object_or_404(UserAccount, user=request.user)
    retailer = get_object_or_404(RetailAccount, user=request.user)
    products = Product.objects.all()
    template = 'retailer_dashboard/dashboard.html'
    context = {
        'retailer': retailer,
        'user': user,
        'products': products,
    }
    return render(request, template, context)
