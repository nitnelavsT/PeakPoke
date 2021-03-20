from django.shortcuts import render
from django.http import HttpResponse

def index(requet):
    return HttpResponse("Salut je suis Article")
