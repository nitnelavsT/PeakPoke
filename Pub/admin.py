from django.contrib import admin
from .models import Pub

class PubAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur')

admin.site.register(Pub,PubAdmin)
