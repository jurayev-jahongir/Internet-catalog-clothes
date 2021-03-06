# Generated by Django 4.0.5 on 2022-06-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_network_main_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='О магазине')),
                ('text', models.TextField(verbose_name='Рассылка')),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'О нас имформация ',
                'verbose_name_plural': 'О нас информации',
            },
        ),
    ]
