from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

from app.views import (
    HomePageView,
)

admin.site.site_header = "Fahrschule Funda Admin"
admin.site.site_title = "Fahrschule Funda Admin Portal"
admin.site.index_title = "Welcome to Fahrschule Funda Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
