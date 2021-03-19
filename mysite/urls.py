from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Client/', include('Client.urls')),
    path('Commandes/', include('Commandes.urls')),
    path('admin/', admin.site.urls),
]