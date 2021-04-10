from django.shortcuts import render
from django.http import HttpResponse
from Pub.models import Pub

def PubView(request):
    pub= Pub.objects.all()
    context= {'pub':pub}
    return render(request, 'Pub/Pub.html', context)

def PubDetail(request, Pub_id):
    pub = Pub.objects.get(pk=Pub_id)
    context= {'pub':pub}
    return render(request, 'Pub/DetailPub.html', context)
