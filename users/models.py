from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(BaseUserManager):
    """Менеджер для кастомной модели пользователя."""
    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает обычного пользователя с заданным email и паролем."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    """Кастомная модель пользователя с email в качестве логина."""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=True, verbose_name='активен')
    is_staff = models.BooleanField(default=False, verbose_name='наличие прав модератора')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='зарегистрирован')
    ROLE_CHOICES = (
        ('subscriber', 'Subscriber'),
        ('author', 'Author'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='subscriber')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} ({self.role})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
