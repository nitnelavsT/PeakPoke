from django.shortcuts import render
from django.http import HttpResponse

def index(request): # pour ne pas laisser de blanc sur la page pub
    return HttpResponse("Salut je suis la Pub")
