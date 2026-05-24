from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from work_profile.forms import (
    UserDataForm,
    WorkProfileForm,
    SocialForm,
    SkillForm,
    LanguageForm,
    WorkExperienceForm,
    EducationExperienceForm
)
from work_profile.models import (
    WorkProfile,
    Social,
    Skill,
    Language,
    WorkExperience,
    EducationExperience
)


class ProfileView(LoginRequiredMixin, DetailView):
    model = WorkProfile
    template_name = "profile/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile, created = WorkProfile.objects.get_or_create(user=self.request.user)

        if not created:
            profile = WorkProfile.objects.prefetch_related(
                "socials", "skills", "languages", "educations", "works"
            ).get(pk=profile.pk)

        return profile


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "profile/profile_update.html"

    def get(self, request, *args, **kwargs):
        user_form = UserDataForm(instance=self.request.user)
        profile_form = WorkProfileForm(instance=self.request.user.workprofile)
        return self.render_to_response(
            context={"user_form": user_form, "profile_form": profile_form}
        )

    def post(self, request, *args, **kwargs):
        user_form = UserDataForm(request.POST, instance=self.request.user)
        profile_form = WorkProfileForm(request.POST, instance=self.request.user.workprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile:profile")
        return self.render_to_response(
            context={"user_form": user_form, "profile_form": profile_form}
        )

class SocialCreateView(LoginRequiredMixin, CreateView):
    model = Social
    form_class = SocialForm
    template_name = "profile/social_form.html"
    success_url = reverse_lazy("profile:profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = Social(profile=self.request.user.workprofile)
        return kwargs


class SocialEditView(LoginRequiredMixin, UpdateView):
    model = Social
    form_class = SocialForm
    template_name = "profile/social_form.html"
    success_url = reverse_lazy("profile:profile")


class SocialDeleteView(LoginRequiredMixin, DeleteView):
    model = Social
    success_url = reverse_lazy("profile:profile")


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = "profile/skill_form.html"
    success_url = reverse_lazy("profile:profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = Skill(profile=self.request.user.workprofile)
        return kwargs


class SkillEditView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = "profile/skill_form.html"
    success_url = reverse_lazy("profile:profile")


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    success_url = reverse_lazy("profile:profile")


class LanguageCreateView(LoginRequiredMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = "profile/language_form.html"
    success_url = reverse_lazy("profile:profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = Language(profile=self.request.user.workprofile)
        return kwargs


class LanguageEditView(LoginRequiredMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = "profile/language_form.html"
    success_url = reverse_lazy("profile:profile")


class LanguageDeleteView(LoginRequiredMixin, DeleteView):
    model = Language
    success_url = reverse_lazy("profile:profile")


class WorkCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = "profile/work_experience_form.html"
    success_url = reverse_lazy("profile:profile")
    context_object_name = "work_experience"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = WorkExperience(profile=self.request.user.workprofile)
        return kwargs


class WorkEditView(LoginRequiredMixin, UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = "profile/work_experience_form.html"
    success_url = reverse_lazy("profile:profile")
    context_object_name = "work_experience"


class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkExperience
    success_url = reverse_lazy("profile:profile")


class EducationCreateView(LoginRequiredMixin, CreateView):
    model = EducationExperience
    form_class = EducationExperienceForm
    template_name = "profile/education_experience_form.html"
    success_url = reverse_lazy("profile:profile")
    context_object_name = "education_experience"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = EducationExperience(profile=self.request.user.workprofile)
        return kwargs


class EducationEditView(LoginRequiredMixin, UpdateView):
    model = EducationExperience
    form_class = EducationExperienceForm
    template_name = "profile/education_experience_form.html"
    success_url = reverse_lazy("profile:profile")
    context_object_name = "education_experience"


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = EducationExperience
    success_url = reverse_lazy("profile:profile")
