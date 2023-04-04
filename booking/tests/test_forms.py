from django.test import TestCase, Client
from booking.forms import AppointmentForm
from booking.models import Appointment

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


class AppointmentFormLabelTests(TestCase):
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
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")

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


class AppointmentFormValidationTests(TestCase):
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
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")

    def test_form_is_valid(self):
        form_data = {'date': '2023-08-01', 'timeblock': '9 AM'}
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_raises_double_appt_validation(self):
        # test form validation errors
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")
        user = authenticate(username="test_username", password="password")
        data = {
            "date": appt.date,
            "timeblock": appt.timeblock,
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertRaisesMessage(
            ValidationError,
            "Cannot schedule more than one appointment on a single day!",
        )

    def test_form_raises_booked_validation(self):
        # test form validation errors
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")
        data = {
            "date": appt.date,
            "timeblock": appt.timeblock,
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertRaisesMessage(ValidationError, "Sorry, this time is already booked!")


class AppointmentFormValidTest(TestCase):
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
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")

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
