from django.http import HttpResponse
import json

from core import game_logic


def game_config(request):
    if request.method == "POST" and request.is_ajax():
        game_logic.set_game(json.loads(request.body))
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
