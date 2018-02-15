from django.urls import path

from .views import color, default, default_team_name, type_game


urlpatterns = [
    path('type-game', type_game, name='type-game'),
    path('color', color, name='color'),
    path('default-team-name', default_team_name, name='default_team_name'),
    path('default', default, name='default'),
]
