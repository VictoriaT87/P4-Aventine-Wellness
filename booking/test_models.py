from django.test import TestCase
from .models import Account, Appointment


class AppointmentModelTest(TestCase):
    """
    Test Appointment Model
    """
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Appointment.objects.create(date='2023-03-31', timeblock='9 AM', date_posted='2023-03-31')

    def test_date_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_timeblock_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('timeblock').verbose_name
        self.assertEqual(field_label, 'timeblock')

    def test_date_posted_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('date_posted').verbose_name
        self.assertEqual(field_label, 'date posted')

    def test_timeblock_max_length(self):
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field('timeblock').max_length
        self.assertEqual(max_length, 10)

    def test_get_absolute_url(self):
        appointment = Appointment.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(appointment.get_absolute_url(), '/user/user-profile')


class AccountModelTest(TestCase):
    """
    Test Account Model
    """
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Account.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        account = Account.objects.get(id=1)
        field_label = account._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_last_name_label(self):
        account = Account.objects.get(id=1)
        field_label = account._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_first_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 30)