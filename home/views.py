from django.shortcuts import render

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
    Contact Page
    """
    return render(request, "contact.html")
