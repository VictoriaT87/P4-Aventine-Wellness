from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import View, UpdateView, DetailView, DeleteView
from django.contrib import messages

from booking.models import Appointment
from .models import Profile
from .forms import ProfileForm
# Create your views here.


def user_profile(request):
    """
    Show the User's profile - including user info and booked appointments.
    """
    user = request.user

    if request.user.is_authenticated:
        # Render the page for authenticated users.
        appointments = Appointment.objects.filter(user=user).order_by(
            "date", "timeblock"
        )
        return render(
            request,
            "user/user_profile.html",
            {
                "user": user,
                "appointments": appointments,
            },
        )
    else:
        # Redirect anonymous users.
        return HttpResponseRedirect("../../accounts/login/")


class UserEditProfile(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
        ):
    """
    Renders form for editing profile
    """
    model = Profile
    template_name = 'user/user_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('user-profile')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            messages.success(self.request, "Your profile was successfully changed!")
            super().form_valid(form)
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, "Failed to save profile")


class UserDeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes the currently signed-in user and all associated data.
    """

    model = Profile
    template_name = 'user/user_delete.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        Delete Profile for logged in user
        """
        user = self.get_object().user
        user.delete()
        messages.success(self.request, "Profile successfully deleted")
        return HttpResponseRedirect(self.success_url)
