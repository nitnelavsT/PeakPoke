from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Client, Commande
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'Client/index.html'
    context_object_name = 'lastest_Client'

    def get_queryset(self):
        """:return le dernier Client"""
        return Client.objects.order_by('Nom')  # Permet de trier les client par nom


class DetailView(generic.DetailView):
    model = Client
    template_name = 'Client/detail.html'


class MontantView(generic.DetailView):
    model = Client
    template_name = 'Client/Montant.html'


def commande_article(request, Client_id):
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

