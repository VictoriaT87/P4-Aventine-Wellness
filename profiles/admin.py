from django.contrib import admin
from .models import Account
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


admin.site.register(Account)
