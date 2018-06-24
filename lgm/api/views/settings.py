import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils import timezone
from datetime import timedelta

from core import game_logic
from core.conf import core_settings
from core.models import TypeGame, TypeColor, Vest, Game


class GameConfig(View):
    def post(self, request):
        game_logic.set_game(json.loads(request.body))  # TODO check game config
        return HttpResponse('ok')


class GameCMD(View):
    def post(self, request):
        cmd = json.loads(request.body)
        if not ('play' in cmd):
            return HttpResponse('error')

        if cmd['play']:
            game_logic.start_game()
        else:
            game_logic.stop_game()

        return HttpResponse('ok')


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
