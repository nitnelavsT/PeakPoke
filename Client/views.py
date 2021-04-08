from django.http import HttpResponseRedirect
from .models import Client, Commande
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def IndexView(request): # Vue de la page d'accueil du site
    client = Client.objects.all()
    context = {'client': client}
    return render(request, 'Client/ClientList.html', context)



def detail(request, Client_id): #affichage des détails Client
    client = Client.objects.get(pk=Client_id)
    context = {'client': client}
    return render(request, 'Client/DetailC.html', context)



def commande_article(request, Client_id): #affichage des commandes Client
    client = get_object_or_404(Client, pk=Client_id)
    try:
        selected_commande = client.commande_set.get(pk=request.POST['Commande'])
    except (KeyError, Commande.DoesNotExist):
        # Reaffiche les articles de la commande
        return render(request, 'Client/detail.html',
                      {'Client': Client, 'error_message': "Vous n'avez pas selectionner de commande."})
    else:
        selected_commande.Numero_Uniques += 1
        selected_commande.save()
        return HttpResponseRedirect(reverse('Client:Montant', args=(Client_id,)))


