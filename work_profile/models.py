from django.contrib.auth import get_user_model
from django.db import models

from work_profile.choices import (
    NetworkChoice,
    SkillChoice,
    LanguageChoice,
    LanguageLevelChoices,
    DegreeChoices,
)


class WorkProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    desired_position = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Social(models.Model):
    profile = models.ForeignKey(
        WorkProfile, on_delete=models.CASCADE, related_name="socials"
    )
    type = models.CharField(
        max_length=2,
        choices=NetworkChoice.choices,
        default=NetworkChoice.INSTAGRAM
    )
    link = models.URLField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "type"],
                name="unique_social_type_for_user"
            )
        ]

    def __str__(self):
        return f"{self.profile.user.username} - {self.get_type_display()}"


class Skill(models.Model):
    profile = models.ForeignKey(
        WorkProfile, on_delete=models.CASCADE, related_name="skills"
    )
    type = models.CharField(
        max_length=20, choices=SkillChoice.choices, default=SkillChoice.PYTHON
    )
    experience = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "type"], name="unique_skill_type_for_user"
            )
        ]

    def __str__(self):
        return f"{self.profile.user.username} - {self.get_type_display()}"


class Language(models.Model):
    profile = models.ForeignKey(
        WorkProfile, on_delete=models.CASCADE, related_name="languages"
    )
    language = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.ENGLISH
    )
    level = models.CharField(
        max_length=255,
        choices=LanguageLevelChoices.choices,
        default=LanguageLevelChoices.C2,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "language"], name="unique_language_for_user"
            )
        ]

    def __str__(self):
        return f"{self.profile.user.username} - {self.get_language_display()}"


class EducationExperience(models.Model):
    profile = models.ForeignKey(
        WorkProfile, on_delete=models.CASCADE, related_name="educations"
    )
    institution = models.CharField(max_length=255)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)
    degree = models.CharField(
        max_length=5,
        choices=DegreeChoices.choices,
        default=DegreeChoices.BACHELOR
    )
    specialty = models.CharField(max_length=63)

    class Meta:
        ordering = ("-started_at",)

    def __str__(self):
        return f"{self.profile.user.username} - {self.get_degree_display()}"


class WorkExperience(models.Model):
    profile = models.ForeignKey(
        WorkProfile, on_delete=models.CASCADE, related_name="works"
    )
    company = models.CharField(
        max_length=255,
    )
    position = models.CharField(max_length=255)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ("-started_at",)

    def __str__(self):
        return f"{self.profile.user.username} - {self.position}"
