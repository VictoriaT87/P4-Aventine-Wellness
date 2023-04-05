from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):

    list_display = ("user", "first_name", "last_name")