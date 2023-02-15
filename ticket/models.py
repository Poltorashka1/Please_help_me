from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


CustomUser = get_user_model()


class Ticket(models.Model):
    """Модель билета"""
    departure_city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город прибытия',
                                       related_name='departure')
    city_of_arrival = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город отправления',
                                        related_name='arrival')
    time_of_arrival = models.DateTimeField(verbose_name='Время отправки')
    price = models.IntegerField(verbose_name='Цена билета')
    passenger = models.ManyToManyField(CustomUser, related_name='pas', blank=True, null=True)

    def __str__(self):
        """Для нормального отображения в Admin"""
        return f'{self.departure_city}-{self.city_of_arrival}'

    def get_absolute_url(self):
        return reverse('ticket:detail', args=[self.id])


# class Passenger(models.Model):
#     """Модель пассажира"""
#     name = models.CharField(max_length=150, verbose_name='Имя')
#     surname = models.CharField(max_length=150, verbose_name='Фамилия')
#     phone = models.CharField(max_length=150, verbose_name='Номер')
#     email = models.EmailField(unique=True, verbose_name='Почта')
#     register_time = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')
#     ticket = models.ManyToManyField(Ticket, related_name='tik')
#
#     def __str__(self):
#         """Для нормального отображения в Admin"""
#         return self.name


class City(models.Model):
    """Модель города"""
    name = models.CharField(max_length=150, verbose_name='Город')

    def __str__(self):
        """Для нормального отображения в Admin"""
        return self.name
