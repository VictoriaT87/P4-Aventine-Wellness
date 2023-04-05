from django.test import TestCase, Client
from profiles.forms import SignupForm
from profiles.models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class SignUpTest(TestCase):

    def test_signupform(self):
        user = Profile.objects.all()
        data = {
            "username": "Bob",
            "first_name": "Bob",
            "last_name": "Bob",
            "email": "testing@test.com",
            "password1": "randompw",
            "password2": "randompw",
        }
        form = SignupForm(data=data)
        self.assertTrue(form.is_valid())
