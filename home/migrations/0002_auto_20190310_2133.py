# Generated by Django 2.1.7 on 2019-03-10 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]