from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView

from work_profile.forms import UserDataForm, WorkProfileForm
from work_profile.models import WorkProfile


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



