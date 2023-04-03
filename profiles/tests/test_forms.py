from django.test import TestCase, Client
from profiles.forms import SignupForm
from profiles.models import Account

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class SignUpTest(TestCase):

    @classmethod
    def setUp(cls):
        """
        Create a user
        """
        client = Client()
        user = User.objects.create_user(
            username="test_username", email="test@test.com", password="password", first_name="firstname", last_name="lastname"
        )

    def test_signupform(self):
        user = Account.objects.all()
        data = {
            'username': 'Bob',
            'first_name': 'Bob',
            'last_name': 'Bob',
            'email': 'testing@test.com',
            'password1': 'randompw',
            'password2': 'randompw',
        }
        form = SignupForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())
