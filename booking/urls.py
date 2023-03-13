from . import views
from booking.views import (
    AppointmentListView, AppointmentCreateView)
from django.urls import path


urlpatterns = [
    path('', views.HomeTemplate.as_view(), name='home'),
    path('appointment', AppointmentCreateView.as_view(), name='appointment'),
]
