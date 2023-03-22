from allauth.account.forms import SignupForm
from .models import Appointment, Account
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your forms here.

class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    """
    Form for Appointment Model
    """
    # date = forms.DateField(widget=DateInput)
    date = forms.DateField(disabled=True)
    timeblock = forms.CharField(disabled=True)

    class Meta:
        widgets = {'date': DateInput()}
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


class SignupForm(SignupForm):
    """
    Form for custom signup page
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
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