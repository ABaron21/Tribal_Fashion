from django.shortcuts import (render, get_object_or_404, 
                              redirect, reverse)
from profiles.models import UserAccount, RetailAccount


def management_dashboard(request):
    account = get_object_or_404(UserAccount, user=request.user)
    template = 'admin_management/management_dashboard.html'
    context = {
        'account': account
    }
    return render(request, template, context=context)


def retailer_requests(request):
    requests = UserAccount.objects.all()
    template = 'admin_management/retailer_requests.html'
    context = {
        'requests': requests
    }
    return render(request, template, context=context)


def approve_retailer(request, request_user_id):
    account = get_object_or_404(UserAccount, pk=request_user_id)
    account.retailer = True
    account.retailer_requested = False
    account.save()
    return redirect(reverse('retailer_requests'))


def premium_cancel_requests(request):
    requests = RetailAccount.objects.all()
    template = 'admin_management/premium_cancel_requests.html'
    context = {
        'requests': requests
    }
    return render(request, template, context)


def approve_cancelation(request, retailer_id):
    retailer = get_object_or_404(RetailAccount, pk=retailer_id)
    retailer.subscribed = False
    retailer.cancel_subscription = False
    retailer.save()
    return redirect(reverse('premium_cancel_requests'))
