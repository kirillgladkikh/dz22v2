from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории', help_text='Введите наименование категории')
    category_description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта', help_text='Введите наименование продукта')
    product_description = models.TextField(verbose_name='Описание продукта', help_text='Введите описание продукта')
    product_image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Изображение продукта', help_text='Загрузите изображение продукта',)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория продукта', help_text='Введите категорию продукта', null=True, blank=True, related_name="products")  # ТАК ЛИ ???
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания",)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения",)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name', 'product_category']

    def __str__(self):
        return self.product_name