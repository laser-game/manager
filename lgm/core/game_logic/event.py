from ..models import (
    Game,
    Event
)

SCORE_OK = 100
SCORE_FAUL = -50


def evaluate_positon(dat_game: Game):
    players = dat_game.game_player_game.order_by('-points')
    position = 1
    for i in range(len(players)):
        if i > 0 and players[i].points != players[i-1].points:
            position += 1
        players[i].position = position
        players[i].save()


def kill(address1: int, address2: int):
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if dat_game:
        dat_event = Event()
        dat_event.game = dat_game
        dat_event.time = dat_game.elapsed_time
        dat_event.game_player1 = dat_game.game_player_game.filter(vest__address=address1).first()
        dat_event.game_player2 = dat_game.game_player_game.filter(vest__address=address2).first()

        dat_event.game_player1.kills_count += 1
        if (address1 == address2):
            dat_event.game_player1.deaths_count += 1
        else:
            dat_event.game_player2.deaths_count += 1

        if dat_event.game.game_mode == Game.GAME_MODE_TEAM:
            team1_id = dat_event.game.game_team_game.filter(type_color=dat_event.game_player1.type_color).first().id
            team2_id = dat_event.game.game_team_game.filter(type_color=dat_event.game_player2.type_color).first().id
            if team1_id == team2_id:
                dat_event.identifier = Event.TYPE_EVENT_FRIENDLY_FIRE
                dat_event.game_player1.points += SCORE_FAUL
            else:
                dat_event.identifier = Event.TYPE_EVENT_PLAYER_KILL_PLAYER
                dat_event.game_player1.points += SCORE_OK
                dat_event.game_player2.points += SCORE_FAUL
        else:
            if address1 == address2:
                dat_event.identifier = Event.TYPE_EVENT_FRIENDLY_FIRE
                dat_event.game_player1.points += SCORE_FAUL
            else:
                dat_event.identifier = Event.TYPE_EVENT_PLAYER_KILL_PLAYER
                dat_event.game_player1.points += SCORE_OK
                dat_event.game_player2.points += SCORE_FAUL

        dat_event.save()
        dat_event.game_player1.save()
        if address1 != address2:
            dat_event.game_player2.save()
        evaluate_positon(dat_game)
