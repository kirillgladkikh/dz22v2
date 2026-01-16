from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_image',
            'product_category',
            'product_price'
        ]
        labels = {
            'product_name': 'Наименование продукта',
            'product_description': 'Описание продукта',
            'product_image': 'Изображение продукта',
            'product_category': 'Категория продукта',
            'product_price': 'Цена продукта'
        }
        widgets = {
            'product_description': forms.Textarea(attrs={'rows': 3}),
        }
