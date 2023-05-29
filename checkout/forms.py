from django import forms
from .models import Order, ShippingDetails


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country', 'user_account',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'email': 'Email Address',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'county': 'County',
            'user_account': 'User',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
        self.fields['country'].widget.attrs['class'] = 'border-black rounded-0'
        self.fields['user_account'].widget.attrs['hidden'] = True


class ShippingDetailsForm(forms.ModelForm):
    class Meta:
        model = ShippingDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['hidden'] = True
