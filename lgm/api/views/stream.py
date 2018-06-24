from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from core.conf import core_settings
from core.models import TypeGame, TypeColor, Vest, Game


def actual_game(request):
    context = {
        'name': '-',
        'player_count': '-',
        'started_time': '-',
        'elapsed_time': '-',
    }
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).first()
    if dat_game is None:
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
    if dat_game is None:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_DONE).first()
    if dat_game is None:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_BREAK).first()
    if dat_game is None:
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
    if dat_game is None:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_DONE).first()
    if dat_game is None:
        dat_game = Game.objects.order_by('-started_time').filter(state=Game.STATE_BREAK).first()
    if dat_game is None or dat_game.game_mode == Game.GAME_MODE_SOLO:
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
