from django.shortcuts import (render, get_list_or_404, get_object_or_404,
                              redirect, reverse)
from profiles.models import UserAccount, RetailAccount
from products.models import Product
from django.contrib import messages

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


def premium_success(request):
    retailer = get_object_or_404(RetailAccount, user=request.user)
    if request.method == 'POST':
        retailer.subscribed = True
        retailer.save()
        return redirect(reverse('retailer_dashboard'))
    template = 'retailer_dashboard/success.html'
    return render(request, template)


def premium_cancelation(request):
    retailer = get_object_or_404(RetailAccount, user=request.user)
    if request.method == 'POST':
        retailer.cancel_subscription = True
        retailer.save()
        messages.success(request, 'Your premium cancelation request has been sent!')
        return redirect(reverse('retailer_dashboard'))
    template = 'retailer_dashboard/success.html'
