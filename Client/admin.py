from django.contrib import admin

from .models import  Client, Commande
from Article.models import Article




class CommandeInline(admin.TabularInline): #Permet l'affichage de commande sous le Client dans l'interface de gestion de Client
    model = Commande
    extra = 0


class ClientAdmin(admin.ModelAdmin): #Disposition de Client dans l'interface d'administration
    fieldsets = [ #disposition des champs
        ('Identitite', {'fields': ['Nom', 'Prenom','Date_naissance','Adresse','Numero_Telephone','Email']}),
        ('Profession', {'fields': ['Categorie_socioPro', ]}),
    ]
    inlines = [CommandeInline] #affichage de commande en dousous de cette interface


    search_fields = ['Nom','Prenom'] #champs de recherche possible pour les client

admin.site.register(Client, ClientAdmin)


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0

class CommandeAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
