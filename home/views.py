from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

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
            messages.success(
                request, "Your message was sent! We'll be in touch shortly."
            )
            return render(request, "contact.html")
        else:
            messages.error(request, "Failed to send message. Please try again.")

    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)
