# Generated by Django 4.2.1 on 2023-06-14 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_post_data_alter_post_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 6, 14, 19, 12, 25, 797660, tzinfo=datetime.timezone.utc)),
        ),
    ]