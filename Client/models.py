from django.db import models
from datetime import datetime
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

cat_socio = (
    ('un', 'Etudiant'),
    ('deux', 'Cadre'),
    ('trois', 'Professeur')
)

class Client(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_naissance = models.DateField()
    Adresse = models.CharField(max_length= 200, default="")
    Categorie_socioPro = models.CharField(max_length=100, choices= cat_socio)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Numero_Telephone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list




    def __str__(self):
        return '{self.Nom} {self.Prenom}'.format(self=self)


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default= "0")
    Quantite = models.IntegerField()
    Montant = models.FloatField()
    Commande_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True) #liste déroulante des articles.




