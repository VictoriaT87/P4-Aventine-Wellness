from django import forms
from .models import Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AppointmentForm(forms.ModelForm):

    date = forms.DateField(disabled=True)
    timeblock = forms.CharField(disabled=True)

    class Meta:
        model = Appointment
        fields = ('date', 'timeblock',)

