from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from core.conf import core_settings
from core.models import Game


def actual_game(request):
    context = {
        'name': '-',
        'player_count': '-',
        'started_time': '-',
        'elapsed_time': '-',
    }
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if not dat_game:
        return JsonResponse(context, safe=False, json_dumps_params={'indent': 4})

    dat_game.elapsed_time = dat_game.started_time + dat_game.game_duration - timezone.now()
    if dat_game.elapsed_time.total_seconds() < 0:
        dat_game.elapsed_time = timedelta(seconds=0)
    dat_game.save()

    context['name'] = dat_game.name
    context['player_count'] = str(dat_game.player_count)
    if dat_game.started_time is not None:
        context['started_time'] = dat_game.started_time.strftime('%H:%M')
    if dat_game.elapsed_time is not None:
        context['elapsed_time'] = '{:02d}:{:02d}'.format(
            dat_game.elapsed_time.seconds // 60,
            dat_game.elapsed_time.seconds % 60
        )
    return JsonResponse(context, safe=False, json_dumps_params={'indent': 4})


def actual_players(request):
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_DONE).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_BREAK).first()
    if not dat_game:
        return JsonResponse([], safe=False, json_dumps_params={'indent': 4})
    else:
        return JsonResponse(
            [
                {
                    'name': game_player.player.name,
                    'position': game_player.position,
                    'points': game_player.points,
                    'kills_count': game_player.kills_count,
                    'deaths_count': game_player.deaths_count,
                    'color': game_player.type_color.css,
                }
                for game_player in dat_game.game_player_game.order_by('position')
            ],
            safe=False, json_dumps_params={'indent': 4}
        )


def actual_teams(request):
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_DONE).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_BREAK).first()
    if not dat_game or dat_game.game_mode == Game.GAME_MODE_SOLO:
        return JsonResponse([], safe=False, json_dumps_params={'indent': 4})
    else:
        return JsonResponse(
            [
                {
                    'name': game_team.team.name,
                    'position': game_team.position,
                    'points': game_team.points,
                    'kills_count': game_team.kills_count,
                    'deaths_count': game_team.deaths_count,
                    'color': game_team.type_color.css,
                }
                for game_team in dat_game.game_team_game.order_by('position')
            ],
            safe=False, json_dumps_params={'indent': 4}
        )


def actual_events(request):
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_DONE).first()
    if not dat_game:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_BREAK).first()
    if not dat_game:
        return JsonResponse([], safe=False, json_dumps_params={'indent': 4})
    else:
        return JsonResponse(
            [
                {
                    'identifier': event.identifier,
                    'time': '{:02d}:{:02d}'.format(
                        event.time.seconds // 60,
                        event.time.seconds % 60
                    ),
                    'name1': event.game_player1.player.name,
                    'name2': event.game_player2.player.name,
                    'color1': event.game_player1.type_color.css,
                    'color2': event.game_player2.type_color.css
                }
                for event in dat_game.event_game.order_by('time')[:core_settings.MAX_EVENTS]
            ],
            safe=False, json_dumps_params={'indent': 4}
        )
