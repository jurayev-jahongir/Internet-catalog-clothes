# Generated by Django 4.0.5 on 2022-06-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='network',
            new_name='text',
        ),
    ]
