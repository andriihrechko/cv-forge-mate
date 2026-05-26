from django.urls import path

from work_profile.views import (
    ProfileView,
    ProfileUpdateView,
    SocialCreateView,
    SocialEditView,
    SocialDeleteView,
    SkillCreateView,
    SkillEditView,
    SkillDeleteView,
    LanguageCreateView,
    LanguageEditView,
    LanguageDeleteView,
    WorkCreateView,
    WorkEditView,
    WorkDeleteView,
    EducationCreateView,
    EducationEditView,
    EducationDeleteView,
)

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("update/", ProfileUpdateView.as_view(), name="profile-update"),
    path("social/add/", SocialCreateView.as_view(), name="social-create"),
    path(
        "social/<int:pk>/update/",
        SocialEditView.as_view(),
        name="social-update"
    ),
    path(
        "social/<int:pk>/delete/",
        SocialDeleteView.as_view(),
        name="social-delete"
    ),
    path("skill/add/", SkillCreateView.as_view(), name="skill-create"),
    path(
        "skill/<int:pk>/update/",
        SkillEditView.as_view(),
        name="skill-update"
    ),
    path(
        "skill/<int:pk>/delete/",
        SkillDeleteView.as_view(),
        name="skill-delete"
    ),
    path(
        "language/add/",
        LanguageCreateView.as_view(),
        name="language-create"
    ),
    path(
        "language/<int:pk>/update/",
        LanguageEditView.as_view(),
        name="language-update"
    ),
    path(
        "language/<int:pk>/delete/",
        LanguageDeleteView.as_view(),
        name="language-delete",
    ),
    path("work/add/", WorkCreateView.as_view(), name="work-create"),
    path(
        "work/<int:pk>/update/",
        WorkEditView.as_view(),
        name="work-update"
    ),
    path(
        "work/<int:pk>/delete/",
        WorkDeleteView.as_view(),
        name="work-delete"
    ),
    path(
        "education/add/",
        EducationCreateView.as_view(),
        name="education-create"
    ),
    path(
        "education/<int:pk>/update/",
        EducationEditView.as_view(),
        name="education-update",
    ),
    path(
        "education/<int:pk>/delete/",
        EducationDeleteView.as_view(),
        name="education-delete",
    ),
]

app_name = "profile"
