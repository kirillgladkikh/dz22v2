from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache
from django.db import models


def get_products_by_category(category_id):
    """
    Получает список продуктов по ID категории из кэша или из БД.
    :param category_id: ID категории
    :return: QuerySet с продуктами указанной категории
    """
    if not CACHE_ENABLED:
        return Product.objects.filter(product_category_id=category_id).select_related("owner")

    key = f"products_by_category_{category_id}"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.filter(product_category_id=category_id).select_related("owner")
    cache.set(key, products)
    return products


def get_all_categories_with_products_count():
    """
    Возвращает все категории с количеством продуктов в них.
    Используется для навигации.
    """
    return Category.objects.annotate(products_count=models.Count("products")).order_by("category_name")


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products
