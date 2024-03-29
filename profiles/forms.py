from allauth.account.forms import SignupForm
from .models import Profile
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SignupForm(SignupForm):
    """
    Form for custom signup page
    https://django-allauth.readthedocs.io/en/latest/forms.html#signup-allauth-account-forms-signupform
    """

    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    username = forms.CharField(
        max_length=30,
        label="Username",
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )

    def signup(self, request, user):
        # Override the signup form for allauth
        user = super(SignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.save()
        return user

        # Create a user profile based on the SignUpForm
        Profile.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
        )


class ProfileForm(forms.ModelForm):
    """
    Profile Form - shown on Profile Page
    """

    class Meta:
        model = Profile
        fields = ["first_name", "last_name"]
