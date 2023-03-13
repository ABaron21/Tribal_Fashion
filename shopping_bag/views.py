from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_shopping_bag(request):
    template = 'shopping_bag/view_bag.html'
    return render(request, template)


def add_to_bag(request, product_id):
    product = Product.objects.get(pk=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    product_id_str = str(product_id)

    if product_id_str in list(bag.keys()):
        bag[product_id_str] += quantity
        messages.success(request,
                         f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag[product_id] = quantity
        messages.success(request,
                         f'{product.name} has been added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_quantity(request, product_id):
    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
        messages.success(request,
                         f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag.pop(product_id)
        messages.success(request,
                         f'{product.name} has been removed from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(product_id)
        request.session['bag'] = bag
        messages.success(request,
                         f'{product.name} has been removed from your bag!')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing {product.name} from bag!')
        return HttpResponse(status=500)
