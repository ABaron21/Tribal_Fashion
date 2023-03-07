from django.shortcuts import (render, get_object_or_404, redirect, reverse)
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
