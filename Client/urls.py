import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'Client'
urlpatterns = [
    #ex /Client/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.Detail, name='Detail'),
    #path('<int:Client_id>/', views.detail),
    path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns