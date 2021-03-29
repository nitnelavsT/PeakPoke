from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom_article', 'numero_unique')

admin.site.register(Article, ArticleAdmin)
