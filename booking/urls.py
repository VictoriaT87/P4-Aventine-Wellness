from datetime import datetime

from . import views
from booking.views import (
    AppointmentListView, 
    AppointmentCreateView, 
    AppointmentDetailView, 
    AppointmentEditView,
    AppointmentDeleteView, )
from django.urls import path, register_converter


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value


register_converter(DateConverter, "yyyy")

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment', views.appointment, name='appointment'),
    path("appointment/new/", AppointmentCreateView.as_view(), name="appointment-create"),
    path("appointment/<int:pk>/", AppointmentDetailView.as_view(), name="appointment-details"),
    path(
        "appointment/new/<yyyy:date>/",
        AppointmentCreateView.as_view(),
        name="appointment-create-date",
    ),
    path(
        "appointment/new/<yyyy:date>/<str:timeblock>",
        AppointmentCreateView.as_view(),
        name="appointment-create-spec",
    ),
    path("appointment/<int:pk>/edit", AppointmentEditView.as_view(), name="appointment-edit"),
    path("appointment/<int:pk>/delete", AppointmentDeleteView.as_view(), name="appointment-delete"),
    path('user-profile', views.userProfile, name='user-profile'),
]
