# Generated by Django 3.2.6 on 2021-09-04 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210904_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returened'),)},
        ),
    ]
