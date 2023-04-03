from allauth.account.forms import SignupForm
from .models import Appointment
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your forms here


class AppointmentForm(forms.ModelForm):
    """
    Form for Appointment Model
    """

    AVAILABLE_TIMES = (
        ("9 AM", '09:00 - 10:00'),
        ("11 AM", '11:00 - 12:00'),
        ("1 PM", '13:00 - 14:00'),
        ("3 PM", '15:00 - 16:00'),
    )
    
    # date = forms.DateField(widget=DateInput)
    date = forms.DateField()
    timeblock = forms.ChoiceField(choices=AVAILABLE_TIMES)

    class Meta:
        model = Appointment
        fields = ('date', 'timeblock',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        date = cleaned_data.get("date")
        timeblock = cleaned_data.get("timeblock")
        # date = self.cleaned_data['date']

        if Appointment.objects.filter(user=self.user, date=date).exists():
            raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')
        if Appointment.objects.filter(timeblock=timeblock, date=date).exists():
            raise forms.ValidationError('Sorry, this time is already booked!')
        if Appointment.objects.filter(user=user, timeblock=timeblock, date=date).exists():
            raise forms.ValidationError('Sorry, this time is already booked!')

        return cleaned_data
