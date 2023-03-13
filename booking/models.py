from django.db import models
from datetime import datetime, date
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):

    # SERVICES = (
    #     ("Yoga", "Yoga"),
    #     ("Mindfulness Meditation", "Mindfulness Meditation"),
    #     ("Tai Chi", "Tai Chi"),
    #     ("Guided Meditation", "Guided Meditation"),
    # )

    AVAILABLE_TIMES = (
        ("A", '09:00 - 10:00'),
        ("B", '10:30 - 11:30'),
        ("C", '12:00 - 13:00'),
        ("D", '13:30 - 14:30'),
        ("E", '15:00 - 16:00'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # service = models.CharField(max_length=50, choices=SERVICES, default="Yoga")
    
    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=datetime.now)
    timeblock = models.CharField(max_length=10, choices=AVAILABLE_TIMES, default="A")

    def is_upcoming(self):
        return date.today() <= self.date

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("home")
