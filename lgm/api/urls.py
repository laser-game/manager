from django.urls import path

from .views import (
    color,
    vest,
    default,
    default_team_name,
    type_game,
    GameConfig,
    GameCMD,
    actual_game,
    actual_players,
    actual_teams
)


urlpatterns = [
    path('type-game', type_game, name='type-game'),
    path('color', color, name='color'),
    path('vest', vest, name='vest'),
    path('default-team-name', default_team_name, name='default_team_name'),
    path('default', default, name='default'),
    path('game-config', GameConfig.as_view(), name='game_config'),
    path('game-cmd', GameCMD.as_view(), name='game_cmd'),
    path('actual-game', actual_game, name='actual_game'),
    path('actual-players', actual_players, name='actual_players'),
    path('actual-teams', actual_teams, name='actual_teams'),
]
