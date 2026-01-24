from django.contrib import admin
from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "product_price",
        "product_category",
        "product_description",
        "product_image",
        "is_published",  # Добавлено
    )
    list_filter = ("product_category", "is_published")  # Добавлено
    search_fields = (
        "product_name",
        "product_description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
