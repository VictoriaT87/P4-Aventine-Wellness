from . import views
from django.urls import path

from profiles.views import (
    UserDeleteProfile,
    EditProfile
)


urlpatterns = [
    path("user/user-profile", views.user_profile, name="user-profile"),
    path("user/user-update/<int:pk>/", EditProfile.as_view(), name="user-update"),
    path("user/user-delete/<int:pk>/", UserDeleteProfile.as_view(), name="user-delete"),
]