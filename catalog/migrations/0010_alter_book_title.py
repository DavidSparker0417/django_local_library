# Generated by Django 3.2.6 on 2021-09-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
