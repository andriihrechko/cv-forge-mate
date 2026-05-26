from django.db import models
from django.utils.text import slugify


class ResumeTemplate(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    preview_image = models.ImageField(upload_to="templates_preview/", blank=True, null=True)
    html_path = models.CharField(max_length=255, blank=True, null=True)
    css_path = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, default="No description.")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.html_path = f"resumes/{self.slug}.html"
        self.css_path = f"resumes/{self.slug}.css"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
