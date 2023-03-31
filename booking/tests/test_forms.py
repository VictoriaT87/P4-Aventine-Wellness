from django.test import TestCase
from booking.forms import AppointmentForm


class AppointmentFormTest(TestCase):
    def test_appointment_form_date_field_label(self):
        form = AppointmentForm()
        self.assertTrue(form.fields['date'].label is None or form.fields['date'].label == 'date')

    def test_appointment_form_timeblock_field_label(self):
        form = AppointmentForm()
        self.assertTrue(form.fields['timeblock'].label is None or form.fields['timeblock'].label == 'timeblock')

    def test_appointment_form_timeblock_choices(self):
        form = AppointmentForm()
        self.assertTrue(form.fields['timeblock'].label is None or form.fields['timeblock'].label == 'timeblock')