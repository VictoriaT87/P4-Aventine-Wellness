from django.test import TestCase, Client
from home.forms import ContactForm
from home.models import Contact

from django.contrib.auth.models import User


class ContactFormLabelTests(TestCase):
    """
    Test Contact Form is valid
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
        )

    def test_contact_form_date_field_label(self):
        # test field label for date
        form = ContactForm()
        self.assertTrue(
            form.fields["name"].label is None or form.fields["name"].label == "name"
        )

    def test_contact_form_timeblock_field_label(self):
        # test field label for timeblock
        form = ContactForm()
        self.assertTrue(
            form.fields["message"].label is None
            or form.fields["message"].label == "message"
        )


class ContactFormTests(TestCase):
    """
    Test Contact Form
    """

    def test_form_is_valid(self):
        # test contact form is valid
        form_data = {"name": "name", "email": "email@email.com", "message": "test"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
