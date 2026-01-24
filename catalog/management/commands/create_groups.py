from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **options):
        # Получаем модель Product
        product_content_type = ContentType.objects.get(app_label='catalog', model='product')

        # Создаём группу
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует'))

        # Назначаем разрешения
        # 1. Кастомное разрешение can_unpublish_product
        unpublish_perm, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=product_content_type,
        )
        moderator_group.permissions.add(unpublish_perm)

        # 2. Разрешение на удаление продукта (django.contrib.auth)
        delete_perm = Permission.objects.get(
            codename='delete_product',
            # name='Может удалять продукт',
            content_type=product_content_type,
        )
        moderator_group.permissions.add(delete_perm)

        self.stdout.write(
            self.style.SUCCESS(
                'Права "can_unpublish_product" и "delete_product" назначены группе "Модератор продуктов"'
            )
        )


# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import Group, Permission
#
# class Command(BaseCommand):
#     help = 'Создаёт группы пользователей для управления публикациями'
#
#     def handle(self, *args, **options):
#         # Группа «Модератор продуктов»
#         moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
#         if created:
#             self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана'))
#         else:
#             self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует'))
#
#         # Добавьте разрешения (если нужно)
#         # permission = Permission.objects.get(codename='can_publish')
#         # moderator_group.permissions.add(permission)
