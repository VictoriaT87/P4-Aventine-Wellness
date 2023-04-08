from django.contrib import admin
from .models import Appointment

# Register your models here.


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ("user", "date", "timeblock", "date_posted")
    search_fields = ("name", "date", "date_posted")
