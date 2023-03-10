from bootstrap_datepicker_plus.widgets import DatePickerInput

from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('service', 'day', 'time',)
        widgets = {
            "day": DatePickerInput(),
        }
