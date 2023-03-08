from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        catergories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in catergories]

        self.fields['category'].choices = friendly_names
        self.fields['sku'].widget.attrs['value'] = '{{sku}}'
        self.fields['seller'].widget.attrs['value'] = '{{retailer.user.username}}'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
