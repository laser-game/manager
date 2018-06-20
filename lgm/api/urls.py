from django.urls import path

from .views import color, default, default_team_name, type_game, game_config


urlpatterns = [
    path('type-game', type_game, name='type-game'),
    path('color', color, name='color'),
    path('default-team-name', default_team_name, name='default_team_name'),
    path('default', default, name='default'),
    path('game-config', game_config, name='game_config'),
]
