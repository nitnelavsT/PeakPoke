from django.db import models


class Commandes(models.Model):
     Numero_Unique = models.IntegerField()
     Quantie = models.IntegerField()
     Montant = models.FloatField()
     Commande_individu = models.CharField(max_length= 1000)

