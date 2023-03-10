# Generated by Django 4.0 on 2023-02-15 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_arrival', models.DateTimeField(verbose_name='Время отправки')),
                ('price', models.IntegerField(verbose_name='Цена билета')),
                ('city_of_arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='ticket.city', verbose_name='Город отправления')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='ticket.city', verbose_name='Город прибытия')),
            ],
        ),
    ]
