from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Appointment
from django.contrib import messages


# Create your views here.

class HomeTemplate(TemplateView):
    template_name = "index.html"


class AppointmentTemplate(TemplateView):
    template_name = "appointment.html"
