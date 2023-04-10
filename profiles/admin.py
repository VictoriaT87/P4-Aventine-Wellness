from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    """
    Set displays for Profiles on the admin panel
    """
    list_display = ("user", "first_name", "last_name")
