from django import forms
from .models import Product, Category

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
