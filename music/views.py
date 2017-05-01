from django.shortcuts import render

# Create your views here.

# music/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class NightcorePageView(TemplateView):
    template_name = "night.html"

class NCSPageView(TemplateView):
    template_name = "ncs.html"

class aboutncsPageView(TemplateView):
    template_name = "aboutncs.html"

class aboutnightPageView(TemplateView):
    template_name = "aboutnight.html"

class registerPageView(TemplateView):
    template_name = "register.html"

class loginPageView(TemplateView):
    template_name = "login.html"

