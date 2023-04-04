from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from home.views import contact, home, about
from home.forms import ContactForm
from home import views
from http import HTTPStatus
from django.core import mail

from django.http.response import HttpResponseRedirectBase


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def setUp(self):
        self.client = Client()

    def test_home_url_accessible_by_name(self):
        # Test home page renders correctly
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, 'Aventine')

    def test_about_url_accessible_by_name(self):
        # Test about page renders correctly
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_contact_url_accessible_by_name(self):
        # Test contact page renders correctly
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")


class TestContactFormSends(TestCase):
    """
    Testing contact form on contact.html
    """

    def setUp(self):
        # Every test needs access to the request factory.
        client = Client()

    def test_contact_posts_and_redirects(self):
        response = self.client.post(reverse("contact"), {"name": "fred", "email": "test", "message": "test message"})
        self.assertEqual(response.status_code, 200)

    def test(self):
        data = {"name": "fred", "email": "test", "message": "test message"}
        self.client.post(reverse("contact"), data)
        self.assertEqual(response.status_code, 200)