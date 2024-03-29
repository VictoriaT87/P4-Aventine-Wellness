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
        ("9 AM", "09:00 - 10:00"),
        ("11 AM", "11:00 - 12:00"),
        ("1 PM", "13:00 - 14:00"),
        ("3 PM", "15:00 - 16:00"),
    )

    date = forms.DateField()
    timeblock = forms.ChoiceField(choices=AVAILABLE_TIMES)

    class Meta:
        model = Appointment
        fields = (
            "date",
            "timeblock",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        # clean data from form
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        date = cleaned_data.get("date")
        timeblock = cleaned_data.get("timeblock")

        # create error dictionary for validation errors
        error_dict = {}
        if Appointment.objects.filter(user=self.user, date=date).exists():
            # if user has already booked on that date raise validation error
            error_dict["date"] = ValidationError(
                "Cannot schedule more than one appointment on a single day!"
            )
        if Appointment.objects.filter(timeblock=timeblock, date=date).exists():
            # if a time on that day is booked raise validation error
            error_dict["timeblock"] = ValidationError(
                "Sorry, this time is already booked!"
            )

        if error_dict:
            raise ValidationError(error_dict)

        return cleaned_data
