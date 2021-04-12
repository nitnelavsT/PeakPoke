from django.db import models
from tinymce.models import HTMLField 

class Pub(models.Model):
    titre=models.CharField(max_length=255)
    auteur=models.CharField(max_length=255)
    content =  HTMLField()
