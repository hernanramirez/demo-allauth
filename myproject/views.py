# -*- coding: utf-8 -*-

from braces.views import LoginRequiredMixin
from django.views.generic import RedirectView, TemplateView


class Dashboard(LoginRequiredMixin, TemplateView):
    #group_required = u"Administradores"
    template_name = "dashboard.html"
