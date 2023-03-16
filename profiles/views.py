from django.shortcuts import (render, get_object_or_404, redirect, reverse)
from django.contrib.auth.models import User
from .models import UserAccount, RetailAccount
from .forms import UserAccountForm, RetailerRequestForm


def profile(request):
    account = get_object_or_404(UserAccount, user=request.user)
    accountForm = UserAccountForm(instance=account)
    retailerForm = RetailerRequestForm(instance=account)
    template = 'profiles/profile.html'
    context = {
        'account': account,
        'accountForm': accountForm,
        'retailerForm': retailerForm
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
