from django.shortcuts import (render, get_object_or_404, redirect, reverse)
import string
import random
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserAccount

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    query = None
    catergory = None
    seller = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'seller' in request.GET:
            seller = request.GET['seller']
            merchant = 'Tribal Fashion'
            retailer = Q(seller__icontains=merchant)
            if seller == 'Tribal Fashion':
                products = products.filter(retailer)
            elif seller == 'other':
                products = products.exclude(retailer)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria was entered')
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    template = 'products/products.html'
    context = {
        'products': products,
        'search_criteria': query,
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
        cancel_return = 'admin'
    else:
        seller = retailer.user.username
        cancel_return = 'retailer'
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
        'cancel_return': cancel_return,
    }

    return render(request, template, context)
