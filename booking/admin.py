from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ("user", "date", "timeblock", "date_posted")
    search_fields = ("name", "date", "date_posted")
