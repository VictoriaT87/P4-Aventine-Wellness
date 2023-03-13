import datetime

from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View
)


# Create your views here.

class HomeTemplate(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


    # def new_appointment(request):
    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = AppointmentForm()
    # return render(request, 'appointment.html', {'form': form})


class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment.html" 
    context_object_name = "appointment"


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(CreateView):
    form_class = AppointmentForm
    template_name = "appointment.html"

    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = AppointmentForm()
    # return render(request, 'appointment.html', {'form': form})

    def get_initial(self):
        return {
            "day": self.kwargs.get("day"),
            "time": self.kwargs.get("time"),
        }


