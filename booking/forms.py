from django import forms
from .models import Appointment
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your forms here.

class AppointmentForm(forms.ModelForm):

    date = forms.DateField(localize=True)
    timeblock = forms.CharField()

    class Meta:
        model = Appointment
        fields = ('date', 'timeblock',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        date = self.cleaned_data['date']

        if Appointment.objects.filter(user=self.user, date=date).exists():
            raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')
