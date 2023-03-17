# Generated by Django 3.2.18 on 2023-03-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_appointment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeblock',
            field=models.CharField(choices=[('A', '09:00 - 10:00'), ('B', '10:30 - 11:30'), ('C', '12:00 - 13:00'), ('D', '13:30 - 14:30'), ('E', '15:00 - 16:00'), ('F', '16:30 - 17:30')], default='A', max_length=10),
        ),
    ]
