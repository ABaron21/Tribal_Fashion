from django.shortcuts import render, get_object_or_404, redirect, reverse
import string
import random

from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserAccount

# Create your views here.


def add_product(request, retailer_id):
    retailer = get_object_or_404(UserAccount, pk=retailer_id)
    sku = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product', args=[retailer.id]))
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'retailer': retailer,
        'form': form,
        'sku': sku,
    }

    return render(request, template, context)
