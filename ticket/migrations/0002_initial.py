# Generated by Django 4.0 on 2023-02-15 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passenger',
            field=models.ManyToManyField(related_name='pas', to=settings.AUTH_USER_MODEL),
        ),
    ]
