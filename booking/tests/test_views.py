import unittest
from unittest.mock import MagicMock
from unittest.mock import patch, Mock
from django.test import TestCase, Client
from booking.models import Appointment
from booking.views import AppointmentCreateView, AppointmentEditView
from booking.forms import AppointmentForm
from django.urls import reverse
from datetime import datetime
from django.test import RequestFactory

from django.contrib.auth.models import User


class TestSuccessURL(TestCase):
    """
    Testing success_url
    """

    def test_success_url(self):
        # Test success_url redirects correctly
        client = Client()
        user = User.objects.create_user(
            username="test_username", email="test@test.com", password="password",
        )
        self.client.login(username="test_username", password="password")
        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_profile.html')


class TestAppointmentViews(TestCase):
    """
    Testing Appointment Views
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
        appt = Appointment.objects.create(
            id=300, date='2023-05-01', timeblock='9 AM')
       
    def test_appointment_page_redirects_if_logged_in_(self):
        # Test that the appointment page renders if logged in
        self.client.login(username="test_username", password="password")
        response = self.client.get(reverse("appointment"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "appointments/appointment.html")

    def test_appointment_page_redirects_if_not_logged_in_(self):
        # Test that the appointment page redirects if not logged in
        self.client.login(username="wrong_username", password="wrong_password")
        response = self.client.get(reverse("appointment"))
        self.assertRedirects(response, '/accounts/login/',
                             status_code=302, fetch_redirect_response=True)

    def test_appointment_create_url(self):
        # Test that the appointment create url works with intended args
        date = "2023-04-04"
        timeblock = "9 AM"
        self.client.login(username="test_username", password="password")
        self.create_url = reverse(
            'appointment-create-spec', args=[date, timeblock])
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'appointments/appointment_confirm_form.html')

    def test_appointment_edit_url(self):
        # Test that the appointment edit url works with intended args
        appointment = Appointment.objects.create(
            date="2023-04-04", timeblock="9 AM")
        self.client.login(username="test_username", password="password")
        self.edit_url = reverse('appointment-edit', args=[appointment.pk])
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/edit_appointment.html')

    def test_appointment_delete_url(self):
        # Test that the appointment edit url works with intended args
        appointment = Appointment.objects.create(
            date="2023-04-04", timeblock="9 AM")
        self.client.login(username="test_username", password="password")
        self.delete_url = reverse('appointment-delete', args=[appointment.pk])
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'appointments/delete_appointment.html')
