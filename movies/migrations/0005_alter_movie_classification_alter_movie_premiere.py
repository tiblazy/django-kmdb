# Generated by Django 4.1.2 on 2022-10-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_premiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='classification',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='premiere',
            field=models.DateField(default=None),
        ),
    ]