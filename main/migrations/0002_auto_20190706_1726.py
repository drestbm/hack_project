# Generated by Django 2.2.3 on 2019-07-06 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_id', models.BigIntegerField(verbose_name='Глобальный идентификатор')),
                ('name_full', models.CharField(max_length=100, verbose_name='Фирменное наименование юридического лица')),
                ('name_short', models.CharField(max_length=100, verbose_name='Сокращенное наименование')),
                ('name_employee', models.CharField(max_length=100, verbose_name='ФИО руководителя')),
                ('inn', models.CharField(max_length=100, verbose_name='Идентификационный номер налогоплательщика')),
                ('ogrn', models.CharField(max_length=100, verbose_name='ОГРН')),
                ('legal_address', models.CharField(max_length=100, verbose_name='Адрес юридического лица')),
                ('actual_address', models.CharField(max_length=100, verbose_name='Адрес фактического местонахождения органов управления')),
                ('phone', models.CharField(max_length=100, verbose_name='Контактные телефоны')),
                ('email', models.EmailField(max_length=254, verbose_name='Контактные телефоны')),
            ],
            options={
                'verbose_name': 'Управляющая организация',
                'verbose_name_plural': 'Управляющие организации',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='man_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='main.Account'),
        ),
    ]
