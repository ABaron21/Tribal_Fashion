from django.shortcuts import (render, get_object_or_404, 
                              redirect, reverse)
from profiles.models import UserAccount, RetailAccount
from products.models import Product
from checkout.models import OrderLineItem
from django.contrib import messages


def management_dashboard(request):
    account = get_object_or_404(UserAccount, user=request.user)
    products = Product.objects.all()
    template = 'admin_management/management_dashboard.html'
    context = {
        'account': account,
        'products': products
    }
    return render(request, template, context=context)


def remove_tribal_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    items = OrderLineItem.objects.filter(product=product)
    if items:
        messages.error(request, 'An order exists with this item')
        return redirect(reverse('management_dashboard'))
    else:
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect(reverse('management_dashboard'))


def retailer_requests(request):
    requests = UserAccount.objects.all()
    template = 'admin_management/retailer_requests.html'
    context = {
        'requests': requests
    }
    return render(request, template, context=context)


def approve_retailer(request, request_user_id):
    account = get_object_or_404(UserAccount, pk=request_user_id)
    account.retailer = True
    account.retailer_requested = False
    account.save()
    return redirect(reverse('retailer_requests'))


def premium_cancel_requests(request):
    requests = RetailAccount.objects.all()
    template = 'admin_management/premium_cancel_requests.html'
    context = {
        'requests': requests
    }
    return render(request, template, context)


def approve_cancelation(request, retailer_id):
    retailer = get_object_or_404(RetailAccount, pk=retailer_id)
    retailer.subscribed = False
    retailer.cancel_subscription = False
    retailer.save()
    return redirect(reverse('premium_cancel_requests'))
