from django.urls import path

from .apps import WebConfig
from .views import index


app_name = WebConfig.name
urlpatterns = [
    # first has higher priority
    path('settings', index.settings, name='settings'),
    path('stream', index.stream, name='stream'),
    path('archive', index.archive, name='archive'),
    path('', index.index, name='index'),
]
