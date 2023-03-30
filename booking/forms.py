from allauth.account.forms import SignupForm
from .models import Appointment, Account
from django import forms

from django.conf import settings
from bootstrap_datepicker_plus.widgets import DatePickerInput

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your forms here.


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
    date = forms.DateField(disabled=True)
    timeblock = forms.ChoiceField(choices=AVAILABLE_TIMES, disabled=True)

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

        print('clean timeblock: ', timeblock)
        print('clean date: ', date)
        print('Appt exists: ', Appointment.objects.filter(timeblock=timeblock, date=date).exists() )
        # date = self.cleaned_data['date']

        if Appointment.objects.filter(user=self.user, date=date).exists():
            raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')
        if Appointment.objects.filter(timeblock=timeblock, date=date).exists():
            raise forms.ValidationError('Sorry, this time is already booked!')
        if Appointment.objects.filter(user=self.user, timeblock=timeblock, date=date).exists():
            raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')


class SignupForm(SignupForm):
    """
    Form for custom signup page
    """
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=30, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.save()
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name']


class UserDeleteForm(forms.Form):
    """
    Form that adds a checkbox to confirm account deletion
    """
    delete = forms.BooleanField(required=True)