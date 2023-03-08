from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeTemplate.as_view(), name='home'),
    path('appointment', views.AppointmentTemplate.as_view(), name='appointment'),
]
