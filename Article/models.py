from django.db import models
from Client.models import Commande
import uuid

class Article(models.Model):
    #commande_article = models.ForeignKey(Commande, on_delete=models.CASCADE, default= "0")
    #numero_unique = models.CharField(max_length=3, blank=True,editable=False,unique=True, default=create_ref_number())
    numero_unique= models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nom_article = models.CharField(max_length=100)
    quantite_article = models.IntegerField(default=0)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.numero_unique) + str(self.nom_article) + "€" + str(self.prix)
