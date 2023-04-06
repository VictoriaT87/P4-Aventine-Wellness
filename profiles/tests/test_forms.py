from django.test import TestCase, Client
from profiles.forms import SignupForm, ProfileForm
from profiles.models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class TestSignUpForm(TestCase):
    """
    Test SignUp Form
    """

    def test_signupform(self):
        # Test Sign Up Form is valid
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


class TestProfileForm(TestCase):
    """
    Test Profile Form
    """

    def setUp(self):
        """
        Create a user that links to the Profile model
        """
        self.user = User.objects.create_user(username="Bob", password="Test")
        self.profile = Profile.objects.get(user=self.user)

    def test_first_name_label(self):
        # Test first name label shows correctly
        field_label = self.profile._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_first_name_max_length(self):
        # Test first name max length is 10
        max_length = self.profile._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 30)
