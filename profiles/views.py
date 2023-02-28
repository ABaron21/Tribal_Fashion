from django.shortcuts import render, get_object_or_404
from .models import UserAccount
from .forms import UserAccountForm


def profile(request):
    account = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(instance=account)
    template = 'profiles/profile.html'
    context = {
        'account': account,
        'form': form
    }

    return render(request, template, context)
