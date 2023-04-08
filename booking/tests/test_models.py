from django.test import TestCase
from booking.models import Appointment


class AppointmentModelTest(TestCase):
    """
    Test Appointment Model
    """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Appointment.objects.create(
            date="2023-03-31", timeblock="9 AM", date_posted="2023-03-31"
        )

    def test_date_label(self):
        # Test date label shows correctly
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_timeblock_label(self):
        # Test timeblock label shows correctly
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field("timeblock").verbose_name
        self.assertEqual(field_label, "timeblock")

    def test_date_posted_label(self):
        # Test date_posted label shows correctly
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field("date_posted").verbose_name
        self.assertEqual(field_label, "date posted")

    def test_timeblock_max_length(self):
        # Test timeblock max length is 10
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field("timeblock").max_length
        self.assertEqual(max_length, 10)

    def test_get_absolute_url(self):
        # Test absolute URL redirects to user-profile
        appointment = Appointment.objects.get(id=1)
        self.assertEqual(appointment.get_absolute_url(), "/user/user-profile")

    def test_str_return(self):
        # Test str return is correct
        appointment = Appointment.objects.get(id=1)
        self.assertEqual(str(appointment), "None | date: 2023-03-31 | time: 9 AM")
