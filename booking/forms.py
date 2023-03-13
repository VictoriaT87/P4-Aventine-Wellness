from bootstrap_datepicker_plus.widgets import DatePickerInput

from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('day', 'time',)
        widgets = {
            "day": DatePickerInput(attrs={"class": "IE-time"},
        options={
            "format": "DD/MM/YYYY",
                },),
        }

