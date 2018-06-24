from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from core.conf import core_settings
from core.models import TypeGame, TypeColor, Vest, Game


def type_game(request):
    return JsonResponse(
        [
            {
                'name': tg.name,
                'game_mode': tg.game_mode,
                'button_action_mode': tg.button_action_mode,
                'game_duration': int(tg.game_duration.total_seconds()),
                'death_duration': int(tg.death_duration.total_seconds()),
                'batch_shots_count': tg.batch_shots_count,
                'sound_set_type': tg.sound_set_type,
                'enable_sound': tg.enable_sound,
                'enable_vest_light': tg.enable_vest_light,
                'enable_immorality': tg.enable_immorality,
            }
            for tg in TypeGame.objects.all()
        ],
        safe=False, json_dumps_params={'indent': 4}
    )


def color(request):
    return JsonResponse(
        tuple(
            TypeColor.objects.order_by('index').values_list('css', flat=True)
        ),
        safe=False, json_dumps_params={'indent': 4}
    )


def default_team_name(request):
    return JsonResponse(
        tuple(
            TypeColor.objects.order_by('index').values_list('name', flat=True)
        ),
        safe=False, json_dumps_params={'indent': 4}
    )


def vest(request):
    return JsonResponse(
        tuple(
            Vest.objects.order_by('address').filter(enable=True, online=True).values_list('address', flat=True)
        ),
        safe=False, json_dumps_params={'indent': 4}
    )


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


def default(request):
    context = {
        'VEST': tuple(
            Vest.objects.order_by('address').filter(enable=True, online=True).values_list('address', flat=True)
        ),
        'COLOR': tuple(
            TypeColor.objects.order_by('index').values_list('css', flat=True)
        ),
        'DEFAULT_TEAM_NAMES': tuple(
            TypeColor.objects.order_by('index').values_list('name', flat=True)
        ),
        'MIN_PLAYERS': core_settings.MIN_PLAYERS,
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'MIN_NAME_LEN': core_settings.MIN_NAME_LEN,
        'MAX_NAME_LEN': core_settings.MAX_NAME_LEN,
        'MIN_GAME_DURATION': core_settings.MIN_GAME_DURATION,
        'MAX_GAME_DURATION': core_settings.MAX_GAME_DURATION,
        'MIN_DEATH_DURATION': core_settings.MIN_DEATH_DURATION,
        'MAX_DEATH_DURATION': core_settings.MAX_DEATH_DURATION,
        'MIN_SHOTS_IN_BATCH': core_settings.MIN_SHOTS_IN_BATCH,
        'MAX_SHOTS_IN_BATCH': core_settings.MAX_SHOTS_IN_BATCH,
    }
    return JsonResponse(context, safe=False, json_dumps_params={'indent': 4})
