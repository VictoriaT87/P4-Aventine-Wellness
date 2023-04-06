from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    """
    Model for creating an account
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            first_name = instance.first_name
            last_name = instance.last_name
            Profile.objects.create(
                pk=instance.id,
                user=instance,
                first_name=first_name,
                last_name=last_name,
            )

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"Username: {self.user} | First Name: {self.first_name} | Last Name: {self.last_name}"
