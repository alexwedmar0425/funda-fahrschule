from django.contrib import messages
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "Hello http://funda-fahrschule.de")
        return context
