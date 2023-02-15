from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """Расширяем стандартную модель пользователя"""
    username = models.CharField(unique=True, max_length=150)
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    phone = models.CharField(max_length=150, verbose_name='Номер')
    email = models.EmailField(verbose_name='Почта')
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')

    class Meta:
        '''Добавляем разрешения, но впадлу их применять)))'''
        permissions = [
            ('administrator', 'Check_post_comments')
        ]

    def __str__(self):
        """Для нормального отображения в Admin"""
        return self.username
