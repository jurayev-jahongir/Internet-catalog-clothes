# Generated by Django 4.0.5 on 2022-06-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_our'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our',
            name='name',
            field=models.TextField(verbose_name='О магазине'),
        ),
        migrations.AlterField(
            model_name='our',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Рассылка'),
        ),
    ]
