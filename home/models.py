from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "Contact Form Submission"
