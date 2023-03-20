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
        ("9 AM", '09:00 - 10:00'),
        ("11 AM", '11:00 - 12:00'),
        ("1 PM", '13:00 - 14:00'),
        ("3 PM", '15:00 - 16:00'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # service = models.CharField(max_length=50, choices=SERVICES, default="Yoga")
    
    date_posted = models.DateField(default=timezone.now)
    date = models.DateField(default=datetime.now)
    timeblock = models.CharField(max_length=10, choices=AVAILABLE_TIMES, default="9 AM")

    def __str__(self):
        return f"{self.user} | day: {self.date} | time: {self.timeblock}"

    def is_upcoming(self):
        return date.today() <= self.date

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("appointment-details", kwargs={"pk": self.pk})
