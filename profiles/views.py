from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from django.views.generic import View
from django.contrib import messages

from booking.models import Appointment
from .models import Account
from .forms import AccountForm, UserDeleteForm, UserCreationForm

# Create your views here.


def user_profile(request):
    """
    Show the User's profile - including user info and booked appointments.
    """
    user = request.user

    if request.user.is_authenticated:
        # Render the page for authenticated users.
        appointments = Appointment.objects.filter(
            user=user).order_by('date', 'timeblock')
        return render(request, 'user/user_profile.html', {
            'user': user,
            'appointments': appointments,
        })
    else:
        # Redirect anonymous users.
        return HttpResponseRedirect('../accounts/login/')


def user_update(request, id):
    """
    Update the User's profile.
    """
    user = request.user
    appointments = Appointment.objects.filter(
        user=user).order_by('date', 'timeblock')
    form = AccountForm()
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")

            return render(request, 'user/user_profile.html', {
                'user': user,
                'appointments': appointments,
            })
        else:
            messages.warning(request, 'Failed to saved profile')

    return render(request, 'user/user_update.html', {'form': form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, 'user/user_delete.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user = request.user
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('home'))
        return render(request, 'user/user_delete.html', {'form': form})
