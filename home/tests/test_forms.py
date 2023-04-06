from django.test import TestCase, Client
from home.forms import ContactForm
from home.models import Contact


class ContactFormTests(TestCase):
    """
    Test Contact Form labels are valid
    """

    def test_form_is_valid(self):
        form_data = {"name": "name", "email": "email@email.com", "message": "test"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
