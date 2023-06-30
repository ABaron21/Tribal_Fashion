from django.shortcuts import (render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserAccount, RetailAccount
from .forms import UserAccountForm, RetailerRequestForm
from checkout.models import Order, OrderLineItem


@login_required
def profile(request):
    account = get_object_or_404(UserAccount, user=request.user)
    accountForm = UserAccountForm(instance=account)
    retailerForm = RetailerRequestForm(instance=account)
    orders = Order.objects.all()
    user_orders = {}
    order_items = OrderLineItem.objects.all()
    items_ordered = {}
    for order in orders:
        if order.user_account == account.user.username:
            user_orders[order] = order
        for item in order_items:
            if item.order == order:
                items_ordered[order.order_number] = item

    if request.method == 'POST':
        account.user = request.user
        account.first_name = request.POST['first_name']
        account.last_name = request.POST['last_name']
        account.phone_number = request.POST['phone_number']
        account.address = request.POST['address']
        account.postcode = request.POST['postcode']
        account.town_or_city = request.POST['town_or_city']
        account.county = request.POST['county']
        account.country = request.POST['country']
        account.save()
        messages.success(request, 'Account details updated successfully!')
        return redirect(reverse('profile'))

    template = 'profiles/profile.html'
    context = {
        'account': account,
        'accountForm': accountForm,
        'retailerForm': retailerForm,
        'orders': user_orders,
        'order_items': items_ordered
    }

    return render(request, template, context)


@login_required
def retailer_request(request):
    account = get_object_or_404(UserAccount, user=request.user)
    if request.method == 'POST':
        form_data = {
            'user': request.POST['user'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name']
        }
        form = RetailerRequestForm(form_data)
        if form.is_valid():
            form.save()
        account.retailer_requested = True
        account.save()
        messages.success(request, 'Your request has been sent!')
        return redirect(reverse('profile'), args=form)


@login_required
def profile_setup(request):
    user = get_object_or_404(User, pk=request.user.id)
    accountForm = UserAccountForm(initial={
        'user': user,
    })
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    accounts = UserAccount.objects.all()
    for account in accounts:
        if account.user == user:
            return redirect(reverse('profile'))
    template = 'profiles/profile_setup.html'
    context = {
        'user': user,
        'accountForm': accountForm,
    }

    return render(request, template, context)


def order_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    lineitems = OrderLineItem.objects.all()
    template = 'profiles/view_order.html'
    context = {
        'order': order,
        'ordered_items': lineitems,
    }
    return render(request, template, context)


def order_cancel(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order.cancel_request = True
    order.save()
    return_location = ''
    if request.user.is_authenicated:
        return_location = 'profile'
    else:
        return_location = 'home'
    return redirect(reverse(return_location))
