from django.urls import path

from work_profile.views import ProfileView, ProfileUpdateView

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("update/", ProfileUpdateView.as_view(), name="profile-update")
]

app_name = "profile"
