import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views




urlpatterns = [
    path('', views.index),
    path('Client/', include('Client.urls')),
    path('Article/', include('Article.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
