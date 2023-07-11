from django.views.generic.base import TemplateView


class AboutUsView(TemplateView):
    template_name = 'about/index.html'


class WhatWeDoView(TemplateView):
    template_name = 'about/what-we-do.html'


class OurStructureView(TemplateView):
    template_name = 'about/our-structure.html'
