# Generated by Django 3.2.18 on 2023-04-03 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_appointment_days'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
