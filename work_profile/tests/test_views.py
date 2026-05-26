from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from work_profile.models import WorkProfile


class TestProfileViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password"
        )

    def test_profile_view_get_anonymous(self):
        response = self.client.get(reverse("profile:profile"))
        self.assertEqual(response.status_code, 302)

    def test_profile_view_get_authenticated(self):
        self.client.force_login(self.user)

        profile = WorkProfile.objects.create(user=self.user)
        response = self.client.get(reverse("profile:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["profile"], profile)
        self.assertTemplateUsed("profile/profile.html")

    def test_profile_update_get_anonymous(self):
        response = self.client.get(reverse("profile:profile-update"))
        self.assertEqual(response.status_code, 302)

    def test_profile_update_get_authenticated(self):
        self.client.force_login(self.user)

        WorkProfile.objects.create(user=self.user)
        response = self.client.get(reverse("profile:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("user_form", response.context)
        self.assertIn("profile_form", response.context)
