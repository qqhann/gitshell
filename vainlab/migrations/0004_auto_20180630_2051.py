# Generated by Django 2.0.5 on 2018-06-30 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vainlab', '0003_auto_20180630_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_update_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 30, 11, 50, 39, 581730, tzinfo=utc), verbose_name='last time searched for matches'),
        ),
    ]