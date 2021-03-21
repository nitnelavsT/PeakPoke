from django.contrib import admin

from .models import  Client, Commande
from Article.models import Article

#admin.site.register(Client)



class CommandeInline(admin.TabularInline):
    model = Commande
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identitite', {'fields': ['Nom', 'Prenom','Date_naissance','Adresse','Numero_Telephone']}),
        ('Profession', {'fields': ['Categorie_socioPro', ]}),
    ]
    inlines = [CommandeInline]


    search_fields = ['Nom','Prenom']

admin.site.register(Client, ClientAdmin)


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0

class CommandeAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
