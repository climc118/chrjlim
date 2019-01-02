from django.shortcuts import render
from django.views.generic.base import TemplateView

class JanuaryCavernView(TemplateView):
    """View to display January log."""

    template_name = 'january_entry.html'

    def get_context_data(self, **kwargs):
        context = super(JanuaryCavernView, self).get_context_data(**kwargs)
        context['page_title'] = "Cavern | January"
        return context
