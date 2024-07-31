from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv
from django.conf import settings
import os


load_dotenv(settings.BASE_DIR / '.env')


class Command(BaseCommand):
    """Кастомная команда для создания суперпользователя."""

    help = 'Создание суперпользователя'

    def handle(self, *args, **options):
        """Cоздание суперпользователя по данным из файла с настройками (.env)."""
        user = User.objects.create(
            email=os.getenv('ADM_EMAIL'),
            first_name='admin',
            last_name='root',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password(os.getenv('ADM_PSW'))
        user.save()
