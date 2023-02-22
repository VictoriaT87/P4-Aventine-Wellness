from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomeTemplate(TemplateView):
    template_name = 'index.html'


class AppointmentTemplate(TemplateView):
    template_name = 'appointment.html'
