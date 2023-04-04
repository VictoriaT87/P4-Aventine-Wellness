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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message was sent! We'll be in touch shortly."
            )
            return render(request, "contact.html")
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)


# def contact(request):
#     # https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Aventine Contact Email"
#             data = {
#                 "name": form.cleaned_data["name"],
#                 "email": form.cleaned_data["email"],
#                 "message": form.cleaned_data["message"],
#             }
#             message = "\n".join(data.values())

#             try:
#                 send_mail(subject, message, "admin@example.com", ["admin@example.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             messages.success(
#                 request, "Your message was sent! We'll be in touch shortly."
#             )
#             return redirect("contact.html")
#         else:
#             messages.error(request, "Your message failed to send! Please try again.")

#     return render(request, "contact.html", {"form": form})
