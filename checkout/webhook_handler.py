from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order, OrderLineItem
from products.models import Product
import stripe
import json
import time


class Stripe_Web_Handler:
    """Handles Webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_order_confirmation(self, order):
        customer_email = order.email
        subject = render_to_string(
            "order_confirmation_email/order_confirmation_subject.txt",
            {'order': order})
        body = render_to_string(
            "order_confirmation_email/order_confirmation_body.txt",
            {'order': order,
             'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject=subject,
            message=body,
            recipient_list=[customer_email],
            from_email=settings.DEFAULT_FROM_EMAIL,
        )

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        user_account = intent.metadata.user_account

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[value] = None
        exists = False
        exist_checks = 1
        while exist_checks <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    stripe_pid=pid
                )
                exists = True
                break
            except Order.DoesNotExist:
                exist_checks += 1
                time.sleep(1)
        if exists:
            self._send_order_confirmation(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                     Order exists within the database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    stripe_pid=pid,
                    user_account=user_account
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                        product_seller=product.seller,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_order_confirmation(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
                 SUCCESS: Order has been created',
            status=200)

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
