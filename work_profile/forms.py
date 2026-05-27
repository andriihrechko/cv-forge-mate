from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

from work_profile.models import (
    WorkProfile,
    Social,
    Skill,
    Language,
    WorkExperience,
    EducationExperience,
)
from work_profile.utils.mixins import DateValidationMixin


class UserDataForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class WorkProfileForm(forms.ModelForm):
    class Meta:
        model = WorkProfile
        fields = ("desired_position", "phone_number", "location", "summary")
        widgets = {"summary": forms.Textarea(attrs={"rows": 3})}


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ["type", "link"]

    def clean(self):
        cleaned_data = super().clean()
        social_type = cleaned_data.get("type")
        profile = self.instance.profile
        if profile and social_type:
            exists = (
                Social.objects.filter(profile=profile, type=social_type)
                .exclude(pk=self.instance.pk)
                .exists()
            )
            if exists:
                self.add_error(
                    None,
                    "This social network already exists, "
                    "update it if you want."
                )
        return cleaned_data


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["type", "experience"]

    def clean(self):
        cleaned_data = super().clean()
        skill_type = cleaned_data.get("type")
        profile = self.instance.profile
        if profile and skill_type:
            exists = (
                Skill.objects.filter(profile=profile, type=skill_type)
                .exclude(pk=self.instance.pk)
                .exists()
            )
            if exists:
                self.add_error(
                    None,
                    "This skill already exists, update it "
                    "if you want."
                )
        return cleaned_data


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["language", "level"]

    def clean(self):
        cleaned_data = super().clean()
        language = cleaned_data.get("language")
        profile = self.instance.profile
        if profile and language:
            exists = (
                Language.objects.filter(profile=profile, language=language)
                .exclude(pk=self.instance.pk)
                .exists()
            )
            if exists:
                self.add_error(
                    None,
                    "This language already exists, update "
                    "it if you want."
                )
        return cleaned_data


class WorkExperienceForm(DateValidationMixin, forms.ModelForm):
    started_at = forms.DateField(
        initial=timezone.now,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"],
    )
    ended_at = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = WorkExperience
        fields = [
            "company",
            "position",
            "started_at",
            "ended_at",
            "description"
        ]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class EducationExperienceForm(DateValidationMixin, forms.ModelForm):
    started_at = forms.DateField(
        initial=timezone.now,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"},
            format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"],
    )
    ended_at = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"},
            format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = EducationExperience
        fields = [
            "institution",
            "started_at",
            "ended_at",
            "degree",
            "specialty"
        ]
