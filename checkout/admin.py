from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'total_cost',
                       'overall_total')

    fields = ('order_number', 'full_name', 'phone_number',
              'email', 'street_address1', 'street_address2',
              'postcode', 'town_or_city', 'county', 'country',
              'date', 'total_cost', 'delivery_cost', 'overall_total')

    list_display = ('order_number', 'full_name', 'date',
                    'total_cost', 'delivery_cost', 'overall_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
