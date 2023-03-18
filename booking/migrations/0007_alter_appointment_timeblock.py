# Generated by Django 3.2.18 on 2023-03-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_appointment_timeblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeblock',
            field=models.CharField(choices=[('9 AM', '09:00 - 10:00'), ('11 AM', '11:00 - 12:00'), ('1 PM', '13:00 - 14:00'), ('3 PM', '15:00 - 16:00')], default='9 AM', max_length=10),
        ),
    ]
