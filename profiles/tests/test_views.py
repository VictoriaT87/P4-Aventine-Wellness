from django.test import TestCase, Client
from profiles.models import Profile
from profiles.views import UserDeleteProfile
from profiles.forms import SignupForm, ProfileForm
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


class TestUserProfile(TestCase):
    """
    Testing User Profile Views
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
            first_name="Bob",
            last_name="Test",
        )

    def test_user_profile_renders_when_logged_in(self):
        # Test user-profile page renders when logged in
        self.client.login(username="test_username", password="password")
        response = self.client.get(reverse("user-profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_profile.html")

    def test_user_profile_redirects_when_not_logged_in(self):
        # Test user-profile page redirects when not logged in
        response = self.client.get(reverse("user-profile"))
        self.assertRedirects(
            response, "/accounts/login/", status_code=302, fetch_redirect_response=True
        )

    def test_update_user_profile_page_renders(self):
        # Test user-profile renders when logged in
        user = self.client.login(username="test_username", password="password")
        response = self.client.post(reverse("user-profile"))
        self.assertEqual(response.status_code, 200)

    def test_update_user_profile_page_updates(self):
        # Test that the user-profile updates
        self.client.login(username="test_username", password="password")
        response = self.client.post(
            reverse("user-profile"), {"first_name": "Bob", "last_name": "last"}
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_user_url(self):
        # Test delete user works and redirects
        self.client.login(username="test_username", password="password")
        self.edit_url = reverse("user-delete", args=[1])
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_delete.html")

    def test_update_user_url(self):
        # Test update user works and redirects
        self.client.login(username="test_username", password="password")
        self.edit_url = reverse("user-update", args=[1])
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/user_update.html")
