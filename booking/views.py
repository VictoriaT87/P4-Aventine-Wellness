from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Appointment
from .forms import AppointmentForm


# Create your views here.

class HomeTemplate(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})