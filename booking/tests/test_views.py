from django.test import TestCase, Client
from booking.models import Appointment
from booking.views import AppointmentCreateView, AppointmentEditView
from booking.forms import AppointmentForm
from django.urls import reverse

from django.contrib.auth.models import User


class TestSuccessURL(TestCase):
    """
    Testing success_url
    """

    def test_success_url(self):
        # Test success_url redirects correctly
        client = Client()
        user = User.objects.create_user(
            username="test_username",
            email="test@test.com",
            password="password",
        )
        self.client.login(username="test_username", password="password")
        url = reverse("user-profile")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


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
        id = 1
        username = "test_username"
        email = "test@test.com"
        password = "password"
        test_user = User.objects.create_user(username, email, password)

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
        self.assertRedirects(
            response, "/accounts/login/",
            status_code=302, fetch_redirect_response=True
        )

    def test_appointment_create_url(self):
        # Test that the appointment create url works with intended args
        date = "2023-04-04"
        timeblock = "9 AM"
        self.client.login(username="test_username", password="password")
        self.create_url = reverse(
            "appointment-create-spec", args=[date, timeblock])
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "appointments/appointment_confirm_form.html")


class TestLoginRequiredPages(TestCase):
    """
    Tests for pages that need a login
    """

    @classmethod
    def setUp(cls):
        """
        Create a user
        """
        client = Client()
        id = 1
        username = "test_username"
        email = "test@test.com"
        password = "password"
        test_user = User.objects.create_user(username, email, password)

    def test_edit_appointment(self):
        # Test that the edit appointment page redirects if logged in
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")
        self.edit_url = reverse("appointment-edit", args=[appt.pk])
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_appointment(self):
        # Test that the delete appointment page redirects if logged in
        appt = Appointment.objects.create(date="2023-05-01", timeblock="9 AM")
        self.edit_url = reverse("appointment-delete", args=[appt.pk])
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)
