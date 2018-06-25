from django.utils import timezone
from datetime import timedelta

from ..models import (
    TypeColor,
    Game,
    TypeGame,
    GamePlayer,
    GameTeam,
    Player, Team,
    Vest
)


def set_game(config):
    game_config = config['SetGame']
    teams = tuple(team for team in config['Team'] if team['enable'])
    players = tuple(player for player in config['Player'] if player['enable'])

    if not players:
        return 'error'

    dat_game = Game()
    dat_game.state = Game.STATE_SET
    dat_game.created_time = timezone.now()

    dat_game.name = game_config['name']
    dat_game.game_mode = game_config['game_mode']
    dat_game.button_action_mode = game_config['button_action_mode']
    dat_game.sound_set_type = game_config['sound_set_type']
    dat_game.game_duration = timedelta(seconds=game_config['game_duration'])
    dat_game.death_duration = timedelta(seconds=game_config['death_duration'])
    dat_game.batch_shots_count = game_config['batch_shots_count']
    dat_game.enable_sound = game_config['enable_sound']
    dat_game.enable_vest_light = game_config['enable_vest_light']
    dat_game.enable_immorality = game_config['enable_immorality']
    dat_game.save()

    teams_names = []
    is_team_game = game_config['game_mode'] == TypeGame.GAME_MODE_TEAM

    if is_team_game:
        for team in teams:
            teams_names.append(team['name'])
            dat_team = Team.objects.filter(name=team['name'])
            if not dat_team.exists():
                dat_team = Team()
                dat_team.name = team['name']
                dat_team.save()
            else:
                dat_team = dat_team.first()

            dat_game_team = GameTeam()
            dat_game_team.game = dat_game
            dat_game_team.team = dat_team
            dat_game_team.type_color = TypeColor.objects.filter(index=team['color_index']).first()
            dat_game_team.position = 1
            dat_game_team.save()

    for player in players:
        dat_player = Player()
        dat_player.name = player['name']
        dat_player.save()

        dat_game_player = GamePlayer()
        dat_game_player.game = dat_game
        dat_game_player.player = dat_player
        dat_game_player.type_color = TypeColor.objects.filter(index=player['color_index']).first()
        dat_game_player.vest = Vest.objects.filter(address=player['address']).first()
        dat_game_player.position = 1
        dat_game_player.points = 0
        dat_game_player.shots_count = 0
        dat_game_player.kills_count = 0
        dat_game_player.deaths_count = 0
        dat_game_player.friendly_kills_count = 0

        if is_team_game:
            dat_game_team = GameTeam.objects.filter(
                type_color__name__in=teams_names,
                type_color__index=player['color_index']
            ).first()
            dat_game_player.team = dat_game_team
        dat_game_player.save()

    return 'ok'
