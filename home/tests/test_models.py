from django.test import TestCase, Client
from home.models import Contact


class AppointmentModelTest(TestCase):
    """
    Test Appointment Model
    """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Contact.objects.create(
            name="Test",
            email="test@test.com",
            date_posted="2023-03-31",
            message="testing",
        )

    def test_name_label(self):
        # Test name label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_email_label(self):
        # Test email label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "email")

    def test_date_posted_label(self):
        # Test date_posted label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("date_posted").verbose_name
        self.assertEqual(field_label, "date posted")

    def test_date_posted_label(self):
        # Test message label shows correctly
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("message").verbose_name
        self.assertEqual(field_label, "message")

    def test_name_max_length(self):
        # Test name max length is 10
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_str_return(self):
        # Test str return is correct
        contact = Contact.objects.get(id=1)
        self.assertEqual(str(contact), "Test, test@test.com")
