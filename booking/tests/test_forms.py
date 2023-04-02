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
            username="test_username", email="test@test.com", password="password",
        )
        appointment = Appointment.objects.create(date="2023-04-04", timeblock="9 AM")

    def test_appointment_form_date_field_label(self):
        # test field label for date
        form = AppointmentForm()
        self.assertTrue(form.fields['date'].label is None or form.fields['date'].label == 'date')

    def test_appointment_form_timeblock_field_label(self):
        # test field label for timeblock
        form = AppointmentForm()
        self.assertTrue(form.fields['timeblock'].label is None or form.fields['timeblock'].label == 'timeblock')

    # def test_appointment_form_timeblock_choices(self):
    #     # test choices for timeblocks
    #     form = AppointmentForm()
    #     self.assertTrue(form.fields['timeblock'].label is None or form.fields['timeblock'].label == 'timeblock')


    def test_appointment_creation(self):
         # test appointment creates through form
        appt = Appointment.objects.create(date='2023-04-01', timeblock='9 AM')
        data = {
            'date': appt.date,
            'timeblock': appt.timeblock,
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        
    def test_valid_form(self):
        appt = Appointment.objects.create(date='2023-04-01', timeblock='9 AM')
        user = User.objects.create(first_name="Bob", last_name="Bob")
        data = {
            'date': appt.date,
            'timeblock': appt.timeblock,
        }
        form = AppointmentForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["date"], ["This field is required."]
        )
        self.assertEqual(
            form.errors["timeblock"], ["This field is required."]
        )
        self.assertRaises(ValidationError, form.clean)
        

    # def test_invalid_form(self):
    #     appt = Whatever.objects.create(title='Foo', body='')
    #     data = {'title': appt.title, 'body': appt.body,}
    #     form = WhateverForm(data=data)
    #     self.assertFalse(form.is_valid())


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='test')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
