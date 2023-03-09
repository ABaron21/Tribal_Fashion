from django.shortcuts import render, redirect

# Create your views here.


def view_shopping_bag(request):
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
