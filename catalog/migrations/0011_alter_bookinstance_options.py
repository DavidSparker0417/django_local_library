# Generated by Django 3.2.6 on 2021-09-06 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_book_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
