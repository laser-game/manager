from django.urls import path

from .views import (
    color,
    vest,
    default,
    default_team_name,
    type_game,
    game_config,
    game_cmd,
    actual_game
)


urlpatterns = [
    path('type-game', type_game, name='type-game'),
    path('color', color, name='color'),
    path('vest', vest, name='vest'),
    path('default-team-name', default_team_name, name='default_team_name'),
    path('default', default, name='default'),
    path('game-config', game_config, name='game_config'),
    path('game-cmd', game_cmd, name='game_cmd'),
    path('actual-game', actual_game, name='actual_game'),
]
