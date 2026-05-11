from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'color']
        widgets = {
            'name':     forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control'}),
            'category': forms.TextInput(attrs={'placeholder': 'Category',     'class': 'form-control'}),
            'price':    forms.NumberInput(attrs={'placeholder': 'Price',      'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity',   'class': 'form-control'}),
            'color':    forms.TextInput(attrs={'placeholder': 'Color',        'class': 'form-control'}),
        }
        error_messages = {
            'name':     {'required': 'Invalid field', 'blank': 'Invalid field'},
            'category': {'required': 'Invalid field', 'blank': 'Invalid field'},
            'price':    {'required': 'Invalid field', 'invalid': 'Invalid field'},
            'quantity': {'required': 'Invalid field', 'invalid': 'Invalid field'},
            'color':    {'required': 'Invalid field', 'blank': 'Invalid field'},
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Invalid field')
        if len(name) < 2:
            raise forms.ValidationError('Invalid field')
        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category or category.strip() == '':
            raise forms.ValidationError('Invalid field')
        return category

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError('Invalid field')
        if price <= 0:
            raise forms.ValidationError('Invalid field')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None:
            raise forms.ValidationError('Invalid field')
        if quantity < 0:
            raise forms.ValidationError('Invalid field')
        return quantity

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if not color or color.strip() == '':
            raise forms.ValidationError('Invalid field')
        if not color.replace(' ', '').isalpha():
            raise forms.ValidationError('Invalid field')
        return color