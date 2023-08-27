from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView

def HomePageView(request):
    return HttpResponse("testing...")
