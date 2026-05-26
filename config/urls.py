from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
    path("profile/", include("work_profile.urls", namespace="profile")),
]
