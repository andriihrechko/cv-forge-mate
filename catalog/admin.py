from django.contrib import admin

from catalog.models import ResumeTemplate


@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ["title", "html_path", "css_path", "is_active"]