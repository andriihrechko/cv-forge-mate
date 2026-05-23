from django.contrib import admin

from work_profile.models import (
    WorkProfile,
    Social,
    Skill,
    Language,
    WorkExperience,
    EducationExperience,
)


@admin.register(WorkProfile)
class WorkProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "desired_position", "phone_number", "location", "summary")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("profile", "type", "link")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("profile", "type", "experience")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("profile", "language", "level")


@admin.register(EducationExperience)
class EducationExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "institution",
        "started_at",
        "ended_at",
        "degree",
        "specialty",
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "company",
        "started_at",
        "ended_at",
        "description",
    )  
