from django.shortcuts import (render, get_object_or_404, redirect, reverse)
import string
import random
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Style
from .forms import ProductForm
from profiles.models import UserAccount

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    query = None
    catergory = None
    seller = None
    style_type = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'style' in request.GET:
            style = request.GET['style'].split(',')
            products = products.filter(style__name__in=style)
            style_type = style

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

    current_sorting = f'{sort}_{direction}'

    template = 'products/products.html'
    context = {
        'products': products,
        'search_criteria': query,
        'style': style_type,
        'current_sorting': current_sorting,
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
    accounts = UserAccount.objects.all()
    retailer = None
    for account in accounts:
        if account.id == retailer_id:
            retailer = account
    if request.user.is_superuser or retailer.retailer:
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
    else:
        messages.error(request, 'You do not have authorization to view this page!')
        return redirect(reverse('home'))


def update_product(request, retailer_id, product_id):
    accounts = UserAccount.objects.all()
    retailer = None
    for account in accounts:
        if account.id == retailer_id:
            retailer = account
    if request.user.is_superuser or retailer.retailer:
        if retailer.user.is_superuser:
            seller = 'Tribal Fashion'
            cancel_return = 'admin'
        else:
            seller = retailer.user.username
            cancel_return = 'retailer'
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            product.category = request.POST['category']
            product.style = request.POST['style']
            product.sku = request.POST['sku']
            product.name = request.POST['name']
            product.image_url = request.POST['image_url']
            product.image = request.POST['image']
            product.description = request.POST['description']
            product.price = request.POST['price']
            product.stock_quantity = request.POST['stock_quantity']
            product.seller = request.POST['seller']
            product.save()
            return redirect(reverse('update_product', args=[retailer.id, product_id]))
        form = ProductForm(initial={
            'category': product.category,
            'style': product.style,
            'sku': product.sku,
            'name': product.name,
            'image_url': product.image_url,
            'image': product.image,
            'description': product.description,
            'price': product.price,
            'stock_quantity': product.stock_quantity,
            'seller': product.seller,
        })
        template = 'products/update_product.html'
        context = {
            'retailer': retailer,
            'form': form,
            'cancel_return': cancel_return,
            'product': product,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You do not have authorization to view this page!')
        return redirect(reverse('home'))
