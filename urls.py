import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views
from apps.common.views import HomeView

from django.views.static import serve
from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='home'),
    #path('', views.index),
    path('Client/', include('Client.urls')),
    path('Article/', include('Article.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
