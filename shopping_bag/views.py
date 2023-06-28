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
        product.stock_quantity = product.stock_quantity - quantity
        product.save()
        messages.success(request,
                         f'Updated {product.name} \
                            quantity to {bag[product_id_str]}')
    else:
        bag[product_id] = quantity
        product.stock_quantity = product.stock_quantity - quantity
        product.save()
        messages.success(request,
                         f'{product.name} has been added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_quantity(request, product_id):
    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product_id_str = str(product_id)
    current_qty = 0
    new_qty = 0

    if quantity > 0:
        current_qty = bag[product_id_str]
        bag[product_id] = quantity
        print(current_qty)
        if quantity > current_qty:
            new_qty = quantity - current_qty
            product.stock_quantity = product.stock_quantity - new_qty
            product.save()
        else:
            new_qty = current_qty - quantity
            product.stock_quantity = product.stock_quantity + new_qty
            product.save()
        messages.success(request,
                         f'Updated {product.name}\
                             quantity to {bag[product_id]}')
    else:
        current_qty = bag[product_id_str]
        bag.pop(product_id)
        new_qty = current_qty - quantity
        product.stock_quantity = product.stock_quantity + new_qty
        product.save()
        messages.success(request,
                         f'{product.name} has been removed from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_id_str = str(product_id)
    current_qty = 0
    try:
        bag = request.session.get('bag', {})
        current_qty = bag[product_id_str]
        bag.pop(product_id)
        product.stock_quantity = product.stock_quantity + current_qty
        product.save()
        request.session['bag'] = bag
        messages.success(request,
                         f'{product.name} has been removed from your bag!')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing {product.name} from bag!')
        return HttpResponse(status=500)
