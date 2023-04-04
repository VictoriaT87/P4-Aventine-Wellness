from django.test import TestCase, Client
from home.forms import Contact
from home.models import Contact


class ContactFormLabelTests(TestCase):
    """
    Test Contact Form labels are valid
    """

    def test_contact_form_name_field_label(self):
        # test field label for name
        form = ContactForm()
        self.assertTrue(
            form.fields["name"].label is None or form.fields["name"].label == "name"
        )

    def test_contact_form_email_field_label(self):
        # test field label for email
        form = ContactForm()
        self.assertTrue(
            form.fields["email"].label is None or form.fields["email"].label == "email"
        )

    def test_contact_form_message_field_label(self):
        # test field label for message
        form = ContactForm()
        self.assertTrue(
            form.fields["message"].label is None
            or form.fields["message"].label == "message"
        )
