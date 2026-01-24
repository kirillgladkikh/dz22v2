from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Создаёт группы пользователей для управления публикациями'

    def handle(self, *args, **options):
        # Группа «Модератор продуктов»
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует'))

        # Добавьте разрешения (если нужно)
        # permission = Permission.objects.get(codename='can_publish')
        # moderator_group.permissions.add(permission)
