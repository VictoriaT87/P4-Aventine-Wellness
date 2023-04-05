from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import View, UpdateView, DetailView
from django.contrib import messages

from booking.models import Appointment
from .models import Profile
from .forms import ProfileForm, UserDeleteForm, UserCreationForm
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


# class ProfileView(DetailView):
#     """
#     Renders profile page view
#     """
#     model = Profile
#     template_name = 'user/user_profile.html'
    

#     def get(self, request, username):
#         """
#         Overides get method. Checks that profile user is current
#         logged in user using username
#         """
#         user = get_object_or_404(User, username=username)
#         profile = Profile.objects.get(user__username=user_id)

#         context = {
#             "account": account,
#         }
#         # If current user is not profile owner returns status 403 forbidden
#         if request.user != account.user:
#             return render(request, '403.html', status=403)

#         return render(request, self.template_name, context)


class EditProfile(
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

    # def test_func(self):
    #     """
    #     Check if the user is the owner of the profile
    #     """
    #     account = self.get_object()
    #     return self.request.user == account.user




# def user_update(request, id):
#     """
#     Update the User's profile.
#     """
#     user = request.user
#     appointments = Appointment.objects.filter(user=user).order_by("date", "timeblock")
#     form = ProfileForm()
#     if request.method == "POST":
#         user = User.objects.get(id=id)
#         user.first_name = request.POST.get("first_name")
#         user.last_name = request.POST.get("last_name")
#         user.save()
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated.")

#             return render(
#                 request,
#                 "user/user_profile.html",
#                 {
#                     "user": user,
#                     "appointments": appointments,
#                 },
#             )
#         else:
#             messages.warning(request, "Failed to saved profile")
#             return render(request, "user/user_update.html", {"form": form})

#     return render(request, "user/user_update.html", {"form": form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        form = UserDeleteForm()
        return render(request, "user/user_delete.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user = request.user
            user.delete()
            messages.success(request, "Profile successfully deleted")
            return redirect(reverse("home"))
        else:
            messages.error(request, "Failed to delete profile.")

        return render(request, "user/user_delete.html", {"form": form})