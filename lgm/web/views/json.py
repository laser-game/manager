from django.http import HttpResponse, JsonResponse

from core.conf import core_settings

def game_types(request):
    fr = open('lgm/web/game-types.json')
    data = fr.readlines()
    fr.close()
    return HttpResponse(data)

def color(request):
    return JsonResponse(core_settings.COLOR, safe=False)
