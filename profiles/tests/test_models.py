from django.test import TestCase
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """
    Test Profile Model
    """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(first_name="Big", last_name="Bob")

    def test_first_name_label(self):
        # Test first name label shows correctly
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_first_name_max_length(self):
        # Test first name max length is 10
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 30)

    def test_last_name_label(self):
        # Test last name label shows correctly
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_first_name_max_length(self):
        # Test last name max length is 10
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 30)
