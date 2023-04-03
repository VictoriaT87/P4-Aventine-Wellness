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


# def contact(request):
#     """
#     Contact Page
#     """
#     def get_success_url(self):
#         return reverse("contact")

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             messages.success(self.request, "Your appointment was successfully booked!")
#             super().form_valid(form)
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return HttpResponseRedirect(self.get_success_url())


# def contact(request):
#     form = ContactForm

#     if request.method == "POST":
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             cd = contact_form.cleaned_data

#             contact = Contact(
#                 name=request.POST.get("name"),
#                 email=request.POST.get("email"),
#                 message=request.POST.get("message"),
#             )
#             contact.save()
#             messages.success(
#                    request, "Message sent! We'll be in touch soon.")

#             return render(
#                     request,
#                    "contact.html",
#                     )
#         else:
#             messages.warning(
#                 request, "Failed to send message. Please try again.")

#     return render(request, "contact.html", {"form": form})


def contact(request):
    # https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Aventine Contact Email"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "admin@example.com", ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(
                request, "Your message was sent! We'll be in touch shortly."
            )
            return redirect("contact")
        else:
            messages.error(request, "Your message failed to send! Please try again.")

    form = ContactForm()
    return render(request, "contact.html", {"form": form})
