from django.forms import ModelForm
from .models import Commande

class ArticleForm(ModelForm):
    class Meta:
        model = Commande
        fields = ['Numero_Unique', 'Commande_individu']

