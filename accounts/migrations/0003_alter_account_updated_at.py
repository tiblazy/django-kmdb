# Generated by Django 4.1.2 on 2022-10-10 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_bio_alter_account_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 18, 24, 54, 505173)),
        ),
    ]