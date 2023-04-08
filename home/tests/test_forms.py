from django.test import TestCase
from home.forms import ContactForm
from home.models import Contact


class ContactFormTests(TestCase):
    """
    Test Contact Form
    """

    def test_form_is_valid(self):
        # test contact form is valid
        form_data = {"name": "name", "email": "email@email.com", "message": "test"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
