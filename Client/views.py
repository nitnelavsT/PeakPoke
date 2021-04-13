from django.http import HttpResponseRedirect
from .models import Client, Commande
from Article.models import Article
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

Total=0

def IndexView(request): # Vue de la page d'accueil du site
    client = Client.objects.all()
    context = {'client': client}
    return render(request, 'Client/ClientList.html', context)



def detail(request, Client_id): #affichage des détails Client
    client = Client.objects.get(pk=Client_id)
    commandes = Commande.objects.all()
    #commande=Commande.objects.get(pk=Commande_id)
    contexts = {'client': client, 'commandes': commandes}

    return render(request, 'Client/DetailC.html', contexts)



def commande_article(request, Article_id, Commande_id): #affichage des commandes Client
    articles=Article.objects.get(pk=Article_id)
    commandes= Commande.objects.get(pk=Commande_id)
    return render(request, 'Client/Commande.html', {'articles': articles, 'commandes': commandes})


