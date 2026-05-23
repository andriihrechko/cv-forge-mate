from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class AboutView(TemplateView):
    template_name = "catalog/about.html"
