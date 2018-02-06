from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('game-types', views.settings_game_types, name='settings game types'),
    path('stream', views.stream, name='stream'),
    path('archive', views.archive, name='archive'),
]
