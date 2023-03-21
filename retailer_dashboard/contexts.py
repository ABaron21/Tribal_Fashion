from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404, HttpResponse
from profiles.models import RetailAccount
from products.models import Product
from checkout.models import OrderLineItem


def retailer_wallet(request):
    user_authenticathed = True if request.user.is_authenticated else False
    if user_authenticathed:
        retailer = get_object_or_404(RetailAccount, user=request.user)
        total = 10
        wallet_fee = 0
        products_sold = OrderLineItem.objects.all()

        for item in products_sold:
            if item.seller == retailer.user.username:
                total += item.lineitem_total

        if retailer.subscribed is True:
            wallet_fee = 0
        else:
            wallet_fee = total * Decimal(settings.SITE_FEE_PERCENTAGE / 100)

        wallet_total = total - wallet_fee

        context = {
            'total': total,
            'wallet_fee': wallet_fee,
            'wallet_total': wallet_total
        }

        return context
    else:
        context = {}
        return context
