from django.http import JsonResponse

from core.conf import core_settings
from core.models import TypeGame, TypeColor


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
    return JsonResponse(list(TypeColor.objects.all().order_by('index').values_list('css', flat=True), safe=False))


def default_team_name(request):
    return JsonResponse(list(TypeColor.objects.all().order_by('index').values_list('name', flat=True), safe=False))


def default(request):
    context = {
        'COLOR': list(TypeColor.objects.all().order_by('index').values_list('css', flat=True)),
        'DEFAULT_TEAM_NAMES': list(TypeColor.objects.all().order_by('index').values_list('name', flat=True)),
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
