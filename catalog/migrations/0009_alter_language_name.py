# Generated by Django 3.2.6 on 2021-09-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text="Select the book's natural language (e.g. Eglish, French, Japanese etc.)", max_length=64, unique=True),
        ),
    ]
