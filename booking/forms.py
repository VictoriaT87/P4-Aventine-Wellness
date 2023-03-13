from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    date = forms.DateField(disabled=True)

    class Meta:
        model = Appointment
        fields = ('date', 'timeblock',)

