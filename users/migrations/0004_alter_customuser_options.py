# Generated by Django 4.0 on 2023-02-15 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('administrator', 'Check_post_comments')]},
        ),
    ]
