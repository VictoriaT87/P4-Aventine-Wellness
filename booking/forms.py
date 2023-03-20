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
        # self.fields['date'].widget = forms.TextInput(
        #     attrs={'date': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        date = self.cleaned_data['date']
        # date = cleaned_data.get("date")
        # timeblock = cleaned_data.get("timeblock")


        if Appointment.objects.filter(user=self.user, date=date).exists():
            raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')

        # if Appointment.objects.filter(user=user).exclude(date=date):
        #     raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')

        # if Appointment.objects.filter(user=self.request.user).exists():
        #     if Appointment.objects.filter(date=self.data['date']).exists():
        #         raise forms.ValidationError('Cannot schedule more than one appointment on a single day!')

        # if Appointment.objects.filter(user=self.data.get('user')).exists():            
        #     if Appointment.objects.filter(date=self.data['date']).exclude('date'):
        #         raise ValidationError(
        #            "Cannot schedule more than one appointment on a single day!"
        #         )
        #     if Appointment.objects.filter(date=self.date, timeblock=self.timeblock).exists():
        #         raise forms.ValidationError("That date & time is already booked!")

    # def clean(self):
    #     if Appointment.objects.filter(user=self.data['user'], date=self.data['date']).exists():
    #         raise forms.ValidationError(
    #             "Cannot schedule more than one Appointment on a single day!"
    #         )
    #     if Appointment.objects.filter(date=self.date, timeblock=self.timeblock).exists():
    #         raise forms.ValidationError("That date & time is already booked!")
