from django.contrib import admin
from .models import Client, Commande
from Article.models import Article
from Pub.models import Pub



class CommandeInline(admin.TabularInline): #Permet l'affichage de commande sous le Client dans l'interface de gestion de Client
    model = Commande
    extra = 0

class ArticleInline(admin.TabularInline): #Disposition de Client dans l'interface d'administration
    model = Article
    extra = 0


class ClientAdmin(admin.ModelAdmin):

    #Les champs à afficher sur l'interface
    list_display = ('Nom', 'Prenom')

    #Définition des catégorie de champs
    fieldsets = [
        ('Identitite', {'fields': ['Nom', 'Prenom','Date_naissance','numero_de_rue','code_postal','Ville','Numero_Telephone','Email']}),
        ('Profession', {'fields': ['Categorie_socioPro', ]}),
    ]

    #affiche la commande dans l'interface de Client
    inlines = [CommandeInline]

    #Champs pour la recherche de Client
    search_fields = ['Nom','Prenom']

admin.site.register(Client, ClientAdmin)




class CommandeAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]



