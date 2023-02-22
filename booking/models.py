from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    AVAILABLE_TIMES = (
        ("9 AM", "9 AM"),
        ("10:30 AM", "10:30 AM"),
        ("12 PM", "12 PM"),
        ("1:30 PM", "1:30 PM"),
        ("3 PM", "3 PM"),
        ("4:30 PM", "4:30 PM"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=AVAILABLE_TIMES, default="9 AM")
