from django.shortcuts import render
from django.views.generic.base import TemplateView, View

class SurfaceHomeView(TemplateView):
    """View to display home page."""

    template_name = 'surface_home.html'

