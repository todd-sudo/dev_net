# Generated by Django 3.2.8 on 2021-10-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'verbose_name': 'Подписчик', 'verbose_name_plural': 'Подписчики'},
        ),
    ]
