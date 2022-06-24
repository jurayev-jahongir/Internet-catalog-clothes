# Generated by Django 4.0.5 on 2022-06-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('network', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]