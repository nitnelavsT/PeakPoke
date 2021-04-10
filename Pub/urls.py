from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.PubView, name="Pub"),
    path('<Pub_id>', views.PubDetail, name="DetailPub"),

]