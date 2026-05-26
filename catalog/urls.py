from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from catalog.views import (
    HomeView,
    AboutView,
    CatalogView,
    TemplateDetailView,
    download_pdf,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path(
        "catalog/template/<slug:slug>/",
        TemplateDetailView.as_view(),
        name="template-detail",
    ),
    path(
        "catalog/template/<slug:slug>/dowload/",
        download_pdf,
        name="download-pdf"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "catalog"
