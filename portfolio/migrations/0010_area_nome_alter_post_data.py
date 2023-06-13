# Generated by Django 4.2.1 on 2023-06-10 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_post_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='nome',
            field=models.CharField(default='Tudo', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 6, 10, 22, 31, 3, 76520, tzinfo=datetime.timezone.utc)),
        ),
    ]