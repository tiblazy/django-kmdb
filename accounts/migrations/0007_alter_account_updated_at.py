# Generated by Django 4.1.2 on 2022-10-11 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 10, 55, 6, 604732)),
        ),
    ]