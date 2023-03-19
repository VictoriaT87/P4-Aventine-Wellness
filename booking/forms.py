from django import forms
from .models import Appointment
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class AppointmentForm(forms.ModelForm):

    date = forms.DateField(disabled=True)
    timeblock = forms.CharField(disabled=True)

    class Meta:
        model = Appointment
        fields = ('date', 'timeblock',)
