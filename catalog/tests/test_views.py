from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from catalog.models import ResumeTemplate


class CatalogViewsTest(TestCase):
    def setUp(self):
        self.template = ResumeTemplate.objects.create(title="Template")
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )

    def test_home_view(self):
        response = self.client.get(reverse("catalog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/home.html")

    def test_about_view(self):
        response = self.client.get(reverse("catalog:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/about.html")

    def test_catalog_view(self):
        response = self.client.get(reverse("catalog:catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/catalog.html")
        self.assertIn("templates", response.context)

    def test_template_detail_view_anonymous(self):
        response = self.client.get(
            reverse(
                "catalog:template-detail",
                kwargs={"slug": self.template.slug}
            )
        )
        self.assertEqual(response.status_code, 302)

    def test_download_pdf_view_anonymous(self):
        response = self.client.get(
            reverse(
                "catalog:download-pdf",
                kwargs={"slug": self.template.slug}
            )
        )
        self.assertEqual(response.status_code, 302)
