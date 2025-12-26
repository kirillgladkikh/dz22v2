from django.core.management import BaseCommand
from django.db import transaction
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории, затем загружает тестовые данные'

    def handle(self, *args, **options):
        self.stdout.write('Начинаем загрузку тестовых данных...')

        # 1. Удаляем все существующие данные
        with transaction.atomic():
            self.stdout.write('Удаляем все категории и продукты...')
            Category.objects.all().delete()
            Product.objects.all().delete()

        # 2. Создаём тестовые категории
        categories = [
            Category(category_name='Электроника', category_description='Электронные устройства'),
            Category(category_name='Одежда', category_description='Одежда и аксессуары'),
            Category(category_name='Книги', category_description='Литературные произведения'),
        ]

        for category in categories:
            category.save()

        self.stdout.write(self.style.SUCCESS(f'Создано категорий: {len(categories)}'))

        # 3. Создаём тестовые продукты
        products = [
            Product(
                product_name='Смартфон X',
                product_description='Современный смартфон с камерой 108 МП',
                product_category=categories[0],
                product_price=49999.99
            ),
            Product(
                product_name='Ноутбук Y',
                product_description='Игровой ноутбук с RTX 4060',
                product_category=categories[0],
                product_price=129999.99
            ),
            Product(
                product_name='Футболка Z',
                product_description='Хлопковая футболка унисекс',
                product_category=categories[1],
                product_price=1499.99
            ),
            Product(
                product_name='Роман "Война и мир"',
                product_description='Классика русской литературы',
                product_category=categories[2],
                product_price=999.99
            ),
        ]

        for product in products:
            product.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Создано продуктов: {len(products)}\n'
                'Загрузка завершена успешно!'
            )
        )
