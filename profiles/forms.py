from allauth.account.forms import SignupForm
from .models import Account
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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