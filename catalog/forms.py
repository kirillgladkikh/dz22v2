from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    # Список запрещённых слов
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
        'бесплатно', 'обман', 'полиция', 'радар'
    ]

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

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Стилизация полей формы
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование продукта...'
        })
        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Опишите продукт...',
            'rows': 6
        })
        self.fields['product_image'].widget.attrs.update({
            'class': 'form-control-file',
            'accept': 'image/*'  # Ограничение на загрузку только изображений
        })
        self.fields['product_category'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Выберите категорию...'
        })
        self.fields['product_price'].widget.attrs.update({
            'class': 'form-control',
            'type': 'number',
            'step': '0.01',  # Для ввода дробных чисел (цена)
            'placeholder': 'Введите цену...'
        })

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if product_name:
            product_name_lower = product_name.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in product_name_lower:
                    raise ValidationError(
                        f'Слово "{word}" запрещено для использования в названии продукта.'
                    )
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get('product_description')
        if product_description:
            product_description_lower = product_description.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in product_description_lower:
                    raise ValidationError(
                        f'Слово "{word}" запрещено для использования в описании продукта.'
                    )
        return product_description

    def clean_product_price(self):
        product_price = self.cleaned_data.get('product_price')
        if product_price is not None:
            if product_price < 0:
                raise ValidationError('Цена не может быть отрицательной! Пожалуйста, введите положительное значение.')
        return product_price

