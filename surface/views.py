from django.shortcuts import render
from django.views.generic.base import TemplateView

class SurfaceHomeView(TemplateView):
    """View to display home page."""

    template_name = 'surface_home.html'

    def get_context_data(self, **kwargs):
        context = super(SurfaceHomeView, self).get_context_data(**kwargs)
        context['page_title'] = "Home"
        return context
