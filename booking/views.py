import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import Appointment, Account
from .forms import AppointmentForm, AccountForm, UserDeleteForm
from django.contrib.auth import logout
from django.contrib import messages

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View
)


# Create your views here.

def home(request):
    return render(request, "index.html")


def appointment(request):
    context = {"days": daylist()}
    return render(request, "appointment.html", context)


def daylist():
    # https://www.geeksforgeeks.org/creating-a-list-of-range-of-dates-in-python/
    res = []
    now = datetime.date.today()
    for days in range(7):
        day = {}
        today = now + datetime.timedelta(days=days)
        weekday = today.strftime("%A").upper()
        day["date"] = str(today)
        day["day"] = weekday
        day["slot1_booked"] = (
            Appointment.objects.filter(date=str(today)).filter(timeblock="9 AM").exists()
        )
        day["slot2_booked"] = (
            Appointment.objects.filter(date=str(today)).filter(timeblock="11 AM").exists()
        )
        day["slot3_booked"] = (
            Appointment.objects.filter(date=str(today)).filter(timeblock="1 PM").exists()
        )
        day["slot4_booked"] = (
            Appointment.objects.filter(date=str(today)).filter(timeblock="3 PM").exists()
        )
        if day["day"] != "SUNDAY":
            res.append(day)
    return res


class AppointmentCreateView(CreateView):
    form_class = AppointmentForm
    template_name = "appointment_confirm_form.html"

    def get_initial(self):
        return {
            "user": self.kwargs.get("user"),
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

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


def user_update(request, id):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('date', 'timeblock')
    form = AccountForm()
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved.')
            return render(request, 'user_profile.html', {
                                'user':user,
                                'appointments':appointments,
                        })
        else:
            messages.warning(request, 'Failed to saved profile')

    return render(request, 'user_update.html', {'form':form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """
    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, 'user_delete.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user = request.user
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('home'))
        return render(request, 'user_delete.html', {'form': form})

