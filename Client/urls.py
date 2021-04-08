import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    #ex /Client/
    path('', views.IndexView, name="Client"), #lien vers l'index du site
    path('<Client_id>', views.detail, name="detailC"), #lien vers les détails clients
    path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG: #outils de débuggage
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
