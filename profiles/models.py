from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    """
    Model for creating an account
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
