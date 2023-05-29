from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm, ShippingDetailsForm
from products.models import Product
from profiles.models import UserAccount
from .models import OrderLineItem, Order, ShippingDetails
from shopping_bag.contexts import shopping_bag_contents
import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'user_account': request.POST['user_account'],
            'full_name': request.POST['full_name'],
            'phone_number': request.POST['phone_number'],
            'email': request.POST['email'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country']
        }
        save_info = request.POST['save-info']
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                    product_seller=product.seller,
                )
                order_line_item.save()
            return redirect(reverse('order_success',
                                    args=[order.order_number, save_info]))
    else:
        bag = request.session.get('bag', {})
        user_authenticathed = True if request.user.is_authenticated else False
        if user_authenticathed:
            username = request.user.username
            user_account = None
            accounts = UserAccount.objects.all()
            for account in accounts:
                if account.user == request.user:
                    user_account = account
            shipping_details = None
            details = ShippingDetails.objects.all()
            for detail in details:
                if detail.user == user_account:
                    shipping_details = detail
            if shipping_details is not None:
                order_form = OrderForm(initial={
                    'user_account': username,
                    'full_name': shipping_details.full_name,
                    'phone_number': shipping_details.phone_number,
                    'email': shipping_details.email,
                    'street_address1': shipping_details.street_address1,
                    'street_address2': shipping_details.street_address2,
                    'postcode': shipping_details.postcode,
                    'town_or_city': shipping_details.town_or_city,
                    'county': shipping_details.county,
                    'country': shipping_details.country
                })
            else:
                order_form = OrderForm(initial={
                    'user_account': username,
                })

        else:
            username = 'Anonymous'
            order_form = OrderForm(initial={
                'user_account': username
            })
        if not bag:
            messages.error(request,
                           'There is nothing in your shopping bag at the \
                            moment!')
            return redirect(reverse('products'))

        shopping_bag = shopping_bag_contents(request)
        total = shopping_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    template = 'checkout/checkout.html'
    context = {
        'form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def order_success(request, order_number, save_info):
    current_order = None
    user_account = None
    if request.user.is_authenticated:
        accounts = UserAccount.objects.all()
        for account in accounts:
            if account.user == request.user:
                user_account = account

    orders = Order.objects.all()
    items_ordered = OrderLineItem.objects.all()
    for order in orders:
        if order.order_number == order_number:
            current_order = order

    print(save_info)
    if save_info:
        print('Saving....')
        shipping_data = {
            'user': user_account,
            'full_name': current_order.full_name,
            'phone_number': current_order.phone_number,
            'email': current_order.email,
            'street_address1': current_order.street_address1,
            'street_address2': current_order.street_address2,
            'postcode': current_order.postcode,
            'town_or_city': current_order.town_or_city,
            'county': current_order.county,
            'country': current_order.country
        }
        shipping_form = ShippingDetailsForm(shipping_data)
        if shipping_form.is_valid():
            shipping_form.save()
    if 'bag' in request.session:
        del request.session['bag']
    template = 'checkout/order_success.html'
    context = {
        'order': current_order,
        'items_ordered': items_ordered
    }
    return render(request, template, context)
