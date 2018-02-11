from django.http import JsonResponse, FileResponse

from api.conf import api_settings
from core.conf import core_settings


def game_types(request):
    # TODO: refactor
    return JsonResponse(api_settings.GAME_TYPES, safe=False)


def color(request):
    return JsonResponse(core_settings.COLOR, safe=False)


def default_team_name(request):
    return JsonResponse(core_settings.DEFAULT_TEAM_NAME, safe=False)


def default(request):
    context = {
        'COLOR': core_settings.COLOR,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
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
