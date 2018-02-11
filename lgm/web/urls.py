from django.urls import path

from .views import index


urlpatterns = [
    path('', index.settings, name='settings'),
    path('settings', index.settings, name='settings'),
    path('stream', index.stream, name='stream'),
    path('archive', index.archive, name='archive'),
]
