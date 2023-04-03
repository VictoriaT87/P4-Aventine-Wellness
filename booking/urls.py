from datetime import datetime

from . import views
from booking.views import (
    AppointmentCreateView,
    AppointmentEditView,
    AppointmentDeleteView,
    )
from django.urls import path, register_converter


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%d-%m-%Y")

    def to_url(self, value):
        return value


register_converter(DateConverter, "yyyy")

urlpatterns = [
    path('appointments/appointment', views.appointment, name='appointment'),
    path('appointments/appointment/new/', AppointmentCreateView.as_view(),
         name='appointment-create'),
    path(
        'appointments/appointment/new/<date>/',
        AppointmentCreateView.as_view(),
        name='appointment-create-date',
    ),
    path(
        'appointments/appointment/new/<date>/<str:timeblock>',
        AppointmentCreateView.as_view(),
        name='appointment-create-spec',
    ),
    path('appointments/appointment/<int:pk>/edit',
         AppointmentEditView.as_view(), name='appointment-edit'),
    path('appointments/appointment/<int:pk>/delete',
         AppointmentDeleteView.as_view(), name='appointment-delete'),
]
