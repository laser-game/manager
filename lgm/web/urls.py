from django.urls import path

from .views import index, json

urlpatterns = [
    path('', index.index, name='index'),
    path('settings', index.settings, name='settings'),
    path('stream', index.stream, name='stream'),
    path('archive', index.archive, name='archive'),

    path('game-types', json.game_types, name='game-types'),
    path('color', json.color, name='color'),
    path('default-team-name', json.default_team_name, name='default_team_name'),
    path('default', json.default, name='default'),
]
