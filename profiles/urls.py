from . import views
from django.urls import path

from profiles.views import (
    UserDeleteView,
)


urlpatterns = [
    path("user/user-profile", views.user_profile, name="user-profile"),
    path("user/user-delete/<int:id>/", UserDeleteView.as_view(), name="user-delete"),
    path("user/user-update/<int:id>/", views.user_update, name="user-update"),
]
