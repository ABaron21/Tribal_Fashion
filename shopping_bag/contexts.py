from django.conf import settings
from decimal import Decimal


def shopping_bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_left = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_left = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'free_delivery_left': free_delivery_left,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context
