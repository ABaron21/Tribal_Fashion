from django.shortcuts import render

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
