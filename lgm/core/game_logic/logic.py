from ..models import TypeColor, Event, TypeEvent, Game, TypeGame, GamePlayer, Player, Switch, TypeGameSwitch, TypeSwitch, Team, Vest

from django.utils import timezone


def set_game(config):
    set_game = config['SetGame']
    players = config['Player']
    teams = config['Team']

    for i in config:
        print('\n======================\n', i, '\n======================')
        for j in config[i]:
            if type(j) is str:
                print(j, config[i][j])
            else:
                print(j)

    print(set_game)
    print(players)
    print(teams)

    dat_game = Game()
    dat_game.type_game = TypeGame.objects.all()[0]
    dat_game.state = 'S'
    dat_game.start = timezone.now()
    dat_game.save()

    for player in players:
        if player['enable']:
            print(player)
            dat_player = Player()
            dat_player.name = player['name']
            dat_player.save()

            color = TypeColor.objects.all().filter(
                index=player['color_index'])[0]
            vest = Vest.objects.all().filter(address=player['address'])[0]

            dat_game_player = GamePlayer()
            dat_game_player.player = dat_player
            dat_game_player.game = dat_game
            dat_game_player.type_color = color
            dat_game_player.vest = vest
            dat_game_player.points = 0
            dat_game_player.shots_count = 0
            dat_game_player.kills_count = 0
            dat_game_player.deaths_count = 0
            dat_game_player.friendly_kills_count = 0
            dat_game_player.save()
