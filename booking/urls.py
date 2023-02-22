from django.urls import path
from .views import HomeTemplate, AppointmentTemplate


urlpatterns = [
    path('', HomeTemplate.as_view(), name='home'),
    path('appointment', AppointmentTemplate.as_view(), name='appointment'),
]
