# Generated by Django 2.2.3 on 2019-07-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190706_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='challenge_done',
            field=models.DateField(default='0001-01-01', verbose_name='Дата выполнения'),
        ),
    ]
