from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date
from work_profile.models import (
    WorkProfile, Social, Skill, Language,
    EducationExperience, WorkExperience
)
from django.db.utils import IntegrityError
from work_profile.choices import (
    NetworkChoice, SkillChoice, LanguageChoice,
    LanguageLevelChoices, DegreeChoices
)

class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="johndoe")
        self.profile = WorkProfile.objects.create(user=self.user)

    def test_work_profile_str(self):
        self.assertEqual(str(self.profile), "johndoe")

    def test_social_str(self):
        social = Social.objects.create(profile=self.profile, type=NetworkChoice.INSTAGRAM, link="http://test.com")
        self.assertEqual(str(social), "johndoe - Instagram")

    def test_skill_str(self):
        skill = Skill.objects.create(profile=self.profile, type=SkillChoice.PYTHON, experience=3)
        self.assertEqual(str(skill), "johndoe - Python")

    def test_language_str(self):
        lang = Language.objects.create(profile=self.profile, language=LanguageChoice.ENGLISH, level=LanguageLevelChoices.C2)
        self.assertEqual(str(lang), "johndoe - English")

    def test_education_experience_str(self):
        edu = EducationExperience.objects.create(
            profile=self.profile, institution="KPI",
            started_at=date(2020, 1, 1), degree=DegreeChoices.BACHELOR, specialty="CS"
        )
        self.assertEqual(str(edu), "johndoe - Bachelor")

    def test_work_experience_str(self):
        work = WorkExperience.objects.create(
            profile=self.profile, company="Google", position="Dev",
            started_at=date(2022, 1, 1), description="Writing code"
        )
        self.assertEqual(str(work), "johndoe - Dev")

    def test_unique_skill_constraint(self):
        Skill.objects.create(
            profile=self.profile, type=SkillChoice.PYTHON, experience=2
        )

        with self.assertRaises(IntegrityError):
            Skill.objects.create(
                profile=self.profile, type=SkillChoice.PYTHON, experience=3
            )

    def test_social_unique_constraint(self):
        Social.objects.create(
            profile=self.profile,
            type=NetworkChoice.INSTAGRAM,
            link="https://instagram.com/user",
        )

        with self.assertRaises(IntegrityError):
            Social.objects.create(
                profile=self.profile,
                type=NetworkChoice.INSTAGRAM,
                link="https://instagram.com/other",
            )