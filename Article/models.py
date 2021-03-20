from django.db import models
from ..Client.models import Commande

class Article(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, default= "0")
    numero_article = models.IntegerField()
    nom_article = models.CharField(max_length=100)
    quantite_article = models.IntegerField(default=0)