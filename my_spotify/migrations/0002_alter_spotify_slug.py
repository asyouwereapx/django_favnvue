# Generated by Django 3.2 on 2021-04-29 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_spotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotify',
            name='slug',
            field=models.SlugField(max_length=30, null=True),
        ),
    ]
