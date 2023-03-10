from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):

    SERVICES = (
        ("Yoga", "Yoga"),
        ("Mindfulness Meditation", "Mindfulness Meditation"),
        ("Tai Chi", "Tai Chi"),
        ("Guided Meditation", "Guided Meditation"),
    )

    AVAILABLE_TIMES = (
        (0, '09:00 - 10:00'),
        (1, '10:30 - 11:30'),
        (2, '12:00 - 13:00'),
        (3, '13:30 - 14:30'),
        (4, '15:00 - 16:00'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICES, default="Yoga")
    day = models.DateField(default=datetime.now)
    time = models.IntegerField(choices=AVAILABLE_TIMES)
