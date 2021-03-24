from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

def index(request):
    template = loader.get_template('Client/home.html')
    return HttpResponse(template.render(request=request))

    #barou
