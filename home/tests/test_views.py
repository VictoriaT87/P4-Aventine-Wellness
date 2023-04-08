from django.test import TestCase, Client
from django.urls import reverse
from home.views import contact, home, about
from home.forms import ContactForm
from home.models import Contact
from home import views


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def setUp(self):
        # set up user
        self.client = Client()

    def test_home_url_accessible_by_name(self):
        # Test home page renders correctly
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Aventine")

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
        # set up user
        client = Client()
        post1 = Contact.objects.create(
            name="Test",
            email="test@test.com",
            message="This is a test to check if a post is correctly created",
        )

    def test_contact_posts_and_redirects(self):
        # Test contact form posts to database
        self.assertEqual(Contact.objects.count(), 1)
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
