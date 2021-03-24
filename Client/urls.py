import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    #ex /Client/
    path('', views.IndexView.as_view(), name="indexC"),
    #path('', views.index),
    path('<Client_id>', views.detail, name="detailC"),
    path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns