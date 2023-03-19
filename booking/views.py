import datetime
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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
        day["slot1_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="9 AM").exists()
        )
        day["slot2_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="11 AM").exists()
        )
        day["slot3_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="1 PM").exists()
        )
        day["slot4_booked"] = (
            Appointment.objects.filter(date=str(curr_day)).filter(timeblock="3 PM").exists()
        )
        if day["day"] != "SUNDAY":
            daylist.append(day)
    return daylist


class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointments.html" 
    context_object_name = "appointments"
    ordering = ["-date"]


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = "appointment_detail.html"


class AppointmentCreateView(CreateView):
    form_class = AppointmentForm
    template_name = "appointment_confirm_form.html"

    def get_initial(self):
        return {
            "user": self.kwargs.get("user"),
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }

    def get_success_url(self):
        return reverse("user-profile")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AppointmentEditView(UpdateView):
    model = Appointment
    template_name = "edit_appointment.html"
    fields = ["date", "timeblock"]
    success_url = reverse_lazy('user-profile')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = "delete_appointment.html"
    success_url = reverse_lazy('user-profile')


def userProfile(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('date', 'timeblock')
    return render(request, 'user_profile.html', {
        'user':user,
        'appointments':appointments,
    })


def home(request):
    return render(request, "index.html")


def appointment(request):
    context = {"days": generate_daylist()}
    return render(request, "appointment.html", context)


def booking(request):
    context = {"booking": Appointment.objects.all()}
    return render(request, "booking.html", context)
