from django.shortcuts import (render, get_object_or_404, redirect, reverse)
from django.contrib.auth.models import User
from .models import UserAccount, RetailAccount
from .forms import UserAccountForm, RetailerRequestForm
from checkout.models import Order, OrderLineItem


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

    template = 'profiles/profile.html'
    context = {
        'account': account,
        'accountForm': accountForm,
        'retailerForm': retailerForm,
        'orders': user_orders,
        'order_items': items_ordered
    }

    return render(request, template, context)


def retailer_request(request):
    account = get_object_or_404(UserAccount, user=request.user)
    if request.method == 'POST':
        form = RetailerRequestForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
        account.retailer_requested = True
        account.save()
        return redirect(reverse('profile'), args=form)


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
    return redirect(reverse('profile'))
