from django.test import TestCase, Client
from booking.models import Account, Appointment
from django.urls import reverse
from datetime import datetime

from django.contrib.auth.models import User


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
            username="test_username", email="test@test.com", password="password"
        )

        

    def test_home_url_accessible_by_name(self):
        # Test home page renders correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_url_accessible_by_name(self):
        # Test about page renders correctly
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_url_accessible_by_name(self):
        # Test contact page renders correctly
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_appointment_page_if_logged_in_(self):
        """
        Test that the appointment page renders
        """
        self.client.login(username="test_username", password="password")
        response = self.client.get(reverse("appointment"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "appointments/appointment.html")

    def test_appointment_page_redirects_if_not_logged_in_(self):
        """
        Test that the appointment page renders
        """
        self.client.login(username="wrong_username", password="wrong_password")
        response = self.client.get(reverse("appointment"))
        self.assertRedirects(response, '/accounts/login/', status_code=302, fetch_redirect_response=True)

    def test_user_profile_renders_when_logged_in(self):
        """
        Test user-profile page renders when logged in
        """
        self.client.login(username="test_username", password="password")
        response = self.client.get(reverse("user-profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_profile.html")

    def test_user_profile_redirects_when_not_logged_in(self):
        # Test contact page renders correctly
        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/', status_code=302, fetch_redirect_response=True)

    # def test_update_appointment(self):
    #     appointment = Appointment.objects.all()
    #     response = self.client.post(
    #         reverse('appointment-edit', kwargs={'pk': pk}), 
    #         {'date': '2023-04-01', 'timeblock': '9 AM'})

    #     self.assertEqual(response.status_code, 302)
    #     assert date == datetime.fromisoformat(date)

