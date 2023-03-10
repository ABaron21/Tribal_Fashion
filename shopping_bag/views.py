from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_shopping_bag(request):
    print(request.session['bag'])
    template = 'shopping_bag/view_bag.html'
    return render(request, template)


def add_to_bag(request, product_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_quantity(request, product_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, product_id):
    try:
        bag = request.session.get('bag', {})
        bag.pop(product_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
