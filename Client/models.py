from django.db import models
from django.core.validators import RegexValidator
from Article.models import Article

cat_socio = (
    ('Etudiant', 'Etudiant'),
    ('Cadre', 'Cadre'),
    ('Professeur', 'Professeur')
)


class Client(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_naissance = models.DateField()
    numero_de_rue = models.DecimalField(decimal_places=0, max_digits=3, default="")
    code_postal = models.DecimalField(max_digits=5, decimal_places=0, default="")
    Ville=models.CharField(max_length=100)
    Categorie_socioPro = models.CharField(max_length=100, choices= cat_socio)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Numero_Telephone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Email = models.EmailField(max_length=254, blank=True)


    # def __str__(self):
    #     return '{self.Nom} {self.Prenom}'.format(self=self)


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default= "0")
    Quantite = models.IntegerField()
    Montant = models.FloatField()
    Commande_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True) #liste déroulante des articles.



