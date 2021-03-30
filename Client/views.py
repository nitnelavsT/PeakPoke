from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Client, Commande
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader


class IndexView(generic.ListView): # Vue de la page d'accueil du site 
    template_name = 'Client/index.html' #le template pour la page d'accueil
    context_object_name = 'lastest_Client' #nom du contexte pour le fichier html (template)

    def get_queryset(self): #méthod de récupération du modèle Client
        """:return le dernier Client"""
        return Client.objects.order_by('Nom')  # Permet de trier les client par nom



def detail(request, Client_id): #affichage des détails Client
    client = Client.objects.get(pk=Client_id)
    message = "Le nom du Client est {}".format(Client.Nom, Client)
    context = dict()
    return render(request, 'Client/index.html', context)



def commande_article(request, Client_id): #affichage des commandes Client
    client = get_object_or_404(Client, pk=Client_id)
    try:
        selected_commande = client.commande_set.get(pk=request.POST['Commande'])
    except (KeyError, Commande.DoesNotExist):
        # Reaffiche les articles de la commande
        return render(request, 'Client/detail.html',
                      {'Client': Client, 'error_message': "Vous n'avez pas selectionner de commande."}) #render : pour lier une méthode à un template
    else:
        selected_commande.Numero_Uniques += 1
        selected_commande.save()
        return HttpResponseRedirect(reverse('Client:Montant', args=(Client_id,)))
