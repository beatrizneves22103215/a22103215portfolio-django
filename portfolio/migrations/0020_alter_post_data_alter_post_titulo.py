# Generated by Django 4.2.1 on 2023-06-14 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 6, 14, 19, 7, 11, 951117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(default='Nenhuma descrição', max_length=100),
        ),
    ]
