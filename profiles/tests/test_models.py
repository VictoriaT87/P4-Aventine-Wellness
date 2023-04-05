from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    """
    Test Profile Model
    """
    def setUp(self):
        """
        Create a user that links to the Profile model
        """
        self.user = User.objects.create_user(
            username='Bob', password='Test'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_first_name_label(self):
        # Test first name label shows correctly
        field_label = self.profile._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_first_name_max_length(self):
        # Test first name max length is 10
        max_length = self.profile._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 30)

    def test_last_name_label(self):
        # Test last name label shows correctly
        field_label = self.profile._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_first_name_max_length(self):
        # Test last name max length is 10
        max_length = self.profile._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 30)
