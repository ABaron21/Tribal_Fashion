from django import forms
from .models import Product, Category, Style


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        catergories = Category.objects.all()
        styles = Style.objects.all()
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in catergories]
        s_friendly_names = [(s.id, s.get_friendly_name()) for s in styles]

        self.fields['category'].choices = c_friendly_names
        self.fields['style'].choices = s_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
