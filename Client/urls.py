from django.urls import path

from . import views

app_name = 'Client'
urlpatterns = [
    #ex /Client/

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/Montant/', views.MontantView.as_view(), name='Montant'),
    path('<int:Client_id>/commande_article/', views.commande_article, name='commande_article'),

]