from django.db import models
from ckeditor.fields import RichTextField

class Pub(models.Model):
    titre=models.CharField(max_length=255)
    body=RichTextField(blank=True, null=True)
    auteur=models.CharField(max_length=255)