from django.test import TestCase, Client
from booking.forms import AppointmentForm, SignupForm
from booking.models import Appointment

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class AppointmentFormTest(TestCase):
    """
    Test Appointment Booking Form is valid
    """

    @classmethod
    def setUp(cls):
        """
        Create a user
        """
        client = Client()
        user = User.objects.create_user(
            username="test_username",
            email="test@test.com",
            password="password",
        )
        appointment = Appointment.objects.create(date="2023-04-04", timeblock="9 AM")

    def test_appointment_form_date_field_label(self):
        # test field label for date
        form = AppointmentForm()
        self.assertTrue(
            form.fields["date"].label is None or form.fields["date"].label == "date"
        )

    def test_appointment_form_timeblock_field_label(self):
        # test field label for timeblock
        form = AppointmentForm()
        self.assertTrue(
            form.fields["timeblock"].label is None
            or form.fields["timeblock"].label == "timeblock"
        )

    def test_form_validation(self):
        # test form validation errors
        appt = Appointment.objects.create(id=300, date="2023-05-01", timeblock="9 AM")
        user = authenticate(username="test_username", password="password")
        data = {
            "date": appt.date,
            "timeblock": appt.timeblock,
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertRaises(ValidationError, form.clean)

    def test_new_appointment_form_is_valid(self):
        # test form is_valid with correct inputs
        form = AppointmentForm(
            data={
                "date": "2023-07-10",
                "timeblock": "9 AM",
            }
        )
        self.assertTrue(form.is_valid())

    def test_new_appointment_form_is_not_valid(self):
        # test form is not valid with wrong inputs
        form = AppointmentForm(
            data={
                "date": "2023-07-10",
                "timeblock": "12 AM",
            }
        )
        self.assertFalse(form.is_valid())
