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
                'enable_sound': tg.enable_sound,
                'enable_vest_light': tg.enable_vest_light,
                'enable_immorality': tg.enable_immorality,
            }
            for tg in TypeGame.objects.all()
        ],
        safe=False
    )


def color(request):
    return JsonResponse(
        tuple(
            TypeColor.objects.order_by('index').values_list('css', flat=True)
        ),
        safe=False
    )


def default_team_name(request):
    return JsonResponse(
        tuple(
            TypeColor.objects.order_by('index').values_list('name', flat=True)
        ),
        safe=False
    )


def vest(request):
    return JsonResponse(
        tuple(
            Vest.objects.order_by('address').filter(enable=True, online=True).values_list('address', flat=True)
        ),
        safe=False
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
        return JsonResponse(context, safe=False)

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
    return JsonResponse(context, safe=False)


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
    return JsonResponse(context, safe=False)
