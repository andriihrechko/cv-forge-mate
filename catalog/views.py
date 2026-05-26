from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views import View
from weasyprint import HTML

from catalog.models import ResumeTemplate


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class AboutView(TemplateView):
    template_name = "catalog/about.html"


class CatalogView(ListView):
    model = ResumeTemplate
    context_object_name = "templates"

    def get_template_names(self):
        if self.request.headers.get("HX-Request"):
            return ["catalog/_result.html"]
        return ["catalog/catalog.html"]

    def get_queryset(self):
        query = self.request.GET.get("query", "").strip()
        if query:
            return ResumeTemplate.objects.filter(title__icontains=query)
        return ResumeTemplate.objects.all()


class TemplateDetailView(LoginRequiredMixin, DetailView):
    model = ResumeTemplate
    context_object_name = "template"
    template_name = "catalog/template_detail.html"


@login_required
def download_pdf(request, slug):
    template = get_object_or_404(ResumeTemplate, slug=slug)
    context = {"template": template}
    html_string = render_to_string("catalog/_pdf_default.html", context, request=request)
    html = HTML(string=html_string, base_url=request.build_absolute_uri("/"))
    pdf = html.write_pdf()

    username = request.user.get_full_name() or "User"
    filename = f"CV.{username}.pdf"

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response