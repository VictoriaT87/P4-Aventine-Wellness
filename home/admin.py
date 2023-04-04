from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ("name", "email", "date_posted")
    search_fields = ("name",)