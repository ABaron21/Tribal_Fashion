from django.shortcuts import (render, get_object_or_404, redirect, reverse)
import string
import random

from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserAccount

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    template = 'products/products.html'
    context = {
        'products': products
    }
    return render(request, template, context=context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    template = 'products/product_detail.html'
    context = {
        'product': product
    }
    return render(request, template, context=context)


def add_product(request, retailer_id):
    retailer = get_object_or_404(UserAccount, pk=retailer_id)
    if retailer.user.is_superuser:
        seller = 'Tribal Fashion'
    else:
        seller = retailer.user.username
    sku = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product', args=[retailer.id]))
    form = ProductForm(initial={
        'sku': sku,
        'seller': seller
    })
    template = 'products/add_product.html'
    context = {
        'retailer': retailer,
        'form': form,
        'sku': sku,
    }

    return render(request, template, context)
