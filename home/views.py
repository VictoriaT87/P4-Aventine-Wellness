from django.shortcuts import render, reverse
from .forms import ContactForm
from django.contrib import messages

from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    """
    Home Page
    """
    return render(request, "index.html")


def about(request):
    """
    About Page
    """
    return render(request, "about.html")


def contact(request):
    """
    Contact Page and Form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thank-you'))
        else:
            messages.error(
                request, "Failed to send message. Please try again. All fields are required.")

    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)


def contact_thank_you(request):
    """
    Conact Thank You Page
    """
    return render(request, "contact_thank_you.html")
