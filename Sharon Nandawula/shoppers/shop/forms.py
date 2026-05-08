from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'quantity', 'color', 'image']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Product Name'}),
            'category': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Category'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Quantity'}),
            'color': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Color'}),
            'image': forms.FileInput(attrs={'class': 'form-input image-input'}),
        }

    def clean_product_name(self):
        value = self.cleaned_data.get('product_name')
        if value and len(value.strip()) < 2:
            raise forms.ValidationError('Product name is too short.')
        return value