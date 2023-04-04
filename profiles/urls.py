from . import views
from django.urls import path

from profiles.views import (
    UserDeleteView,
    UserUpdateAccount
)


urlpatterns = [
    path("user/user-profile", views.user_profile, name="user-profile"),
    path("user/user-update/<int:pk>/edit", UserUpdateAccount.as_view(), name="user-update"),
    path("user/user-delete/<int:pk>", UserDeleteView.as_view(), name="user-delete"),
]
