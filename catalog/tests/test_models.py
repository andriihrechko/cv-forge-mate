from catalog.models import ResumeTemplate
from django.test import TestCase


class TestResumeTemplate(TestCase):
    def setUp(self):
        self.template = ResumeTemplate.objects.create(
            title="Modern Developer CV"
        )

    def test_string_method(self):
        self.assertEqual(str(self.template), "Modern Developer CV")

    def test_slug_generation(self):
        self.assertEqual(self.template.slug, "modern-developer-cv")

    def test_path_generation(self):
        expected_html = "resumes/modern-developer-cv.html"
        expected_css = "resumes/modern-developer-cv.css"

        self.assertEqual(self.template.html_path, expected_html)
        self.assertEqual(self.template.css_path, expected_css)

    def test_default_values(self):
        self.assertEqual(self.template.description, "No description.")
        self.assertTrue(self.template.is_active)
