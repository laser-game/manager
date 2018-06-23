from ..models import (
    TypeColor,
    Event,
    TypeEvent,
    Game,
    TypeGame,
    GamePlayer,
    Player, Switch,
    TypeGameSwitch,
    TypeSwitch,
    Team,
    Vest
)

from django.utils import timezone


def set_game(config):
    set_game = config['SetGame']
    teams = tuple(team for team in config['Team'] if team['enable'])
    players = tuple(player for player in config['Player'] if player['enable'])

    if len(players) == 0:
        return 'error'

    dat_game = Game()
    dat_game.type_game = TypeGame.objects.all().filter(name=set_game['name']).first()
    dat_game.state = 'S'
    dat_game.start = timezone.now()
    dat_game.save()

    if set_game['game_mode'] == 'T':
        teams_names = []
        for team in teams:
            teams_names.append(team['name'])
            dat_team = Team.objects.all().filter(name=team['name'])
            if len(dat_team) == 0:
                dat_team = Team()
                dat_team.name = team['name']
                dat_team.type_color = TypeColor.objects.all().filter(index=team['color_index']).first()
            else:
                dat_team = dat_team.first()
                dat_team.type_color = TypeColor.objects.all().filter(index=team['color_index']).first()
            dat_team.save()

    for player in players:
        dat_player = Player()
        dat_player.name = player['name']
        dat_player.save()

        dat_game_player = GamePlayer()
        dat_game_player.player = dat_player
        dat_game_player.game = dat_game
        dat_game_player.type_color = TypeColor.objects.all().filter(index=player['color_index']).first()
        dat_game_player.vest = Vest.objects.all().filter(address=player['address']).first()
        dat_game_player.points = 0
        dat_game_player.shots_count = 0
        dat_game_player.kills_count = 0
        dat_game_player.deaths_count = 0
        dat_game_player.friendly_kills_count = 0

        if set_game['game_mode'] == 'T':
            dat_team = Team.objects.all().filter(
                type_color__name__in=teams_names,
                type_color__index=player['color_index']
            ).first()
            dat_game_player.team = dat_team

        dat_game_player.save()

    return 'ok'


def start_game():
    dat_game = Game.objects.all().filter(state='S').order_by('-start')
    if len(dat_game) == 0 or len(Game.objects.all().filter(state='P')):
        return 'error'

    dat_game = dat_game.first()
    dat_game.state = 'P'
    dat_game.start = timezone.now()
    dat_game.save()
    return 'ok'


def stop_game():
    dat_game = Game.objects.all().filter(state='P').order_by('-start')
    if len(dat_game) == 0:
        return 'error'

    dat_game = dat_game.first()
    dat_game.state = 'B'
    dat_game.save()
    return 'ok'
