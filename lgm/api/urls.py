from django.urls import path

from .views import color, game_types, default_team_name, default, test

urlpatterns = [
    path('game-types', game_types, name='game-types'),
    path('color', color, name='color'),
    path('default-team-name', default_team_name, name='default_team_name'),
    path('default', default, name='default'),
    path('test', test, name='test'),
]
