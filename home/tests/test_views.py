from django.test import TestCase
from django.urls import reverse


class TestTemplates(TestCase):
    """
    Testing templates render
    """

    def test_home_url_accessible_by_name(self):
        # Test home page renders correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_url_accessible_by_name(self):
        # Test about page renders correctly
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_url_accessible_by_name(self):
        # Test contact page renders correctly
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
