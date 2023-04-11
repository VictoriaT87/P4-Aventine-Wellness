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

    def test_home_url_renders(self):
        # Test home page renders correctly
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_url_template_is_correct(self):
        # Test home page template is correct
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

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

    def test_contact_thank_page_accessible_by_name(self):
        # Test contact thank you page renders correctly
        response = self.client.get(reverse("thank-you"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_thank_you.html")


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

    def test_contact_redirects(self):
        # Test contact form posts is shown
        self.assertEqual(Contact.objects.count(), 1)
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_contact_form_submission(self):
        # Test contact form posts to database
        contact = Contact.objects.last()
        self.assertEqual(contact.name, "Test")
        self.assertEqual(contact.email, "test@test.com")
        self.assertEqual(
            contact.message,
            "This is a test to check if a post is correctly created"
        )
