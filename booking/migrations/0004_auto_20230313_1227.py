# Generated by Django 3.2.18 on 2023-03-13 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20230313_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='day',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='time',
            new_name='timeblock',
        ),
    ]
