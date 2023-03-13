import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
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

# class HomeTemplate(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, "index.html")


def generate_daylist():
    daylist = []
    today = datetime.date.today()
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()
        day["date"] = str(curr_day)
        day["day"] = weekday
        day["A_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="A").exists()
        )
        day["B_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="B").exists()
        )
        day["C_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="C").exists()
        )
        day["D_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="D").exists()
        )
        day["E_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="E").exists()
        )
        if day["day"] != "SATURDAY" or "SUNDAY":  # Writing lab doesn't open on Saturday
            daylist.append(day)
    return daylist


class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment_list.html" 
    context_object_name = "appointment_list"
    ordering = ["-date"]


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(CreateView):
    form_class = AppointmentForm
    template_name = "appointment_list.html"

    def get_initial(self):
        return {
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }


def home(request):
    return render(request, "index.html")


def appointment(request):
    context = {"days": generate_daylist()}
    return render(request, "appointment.html", context)


def booking(request):
    context = {"booking": Appointment.objects.all()}
    return render(request, "booking.html", context)
