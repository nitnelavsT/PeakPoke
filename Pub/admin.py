from django.contrib import admin
from .models import Pub
from tinymce.widgets import TinyMCE
from django.db import models
from django import forms

class PubAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur')
    body = forms.CharField(widget=TinyMCE())

admin.site.register(Pub,PubAdmin)
