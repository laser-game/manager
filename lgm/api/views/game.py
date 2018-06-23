from django.http import HttpResponse
import json

from core import game_logic


def game_config(request):
    if request.method == "POST" and request.is_ajax():
        game_logic.set_game(json.loads(request.body))
        return HttpResponse('ok')
    else:
        return HttpResponse('error')


def game_cmd(request):
    cmd = json.loads(request.body)
    if not ('play' in cmd):
        return HttpResponse('error')

    play = cmd['play']

    if play:
        game_logic.start_game()
    else:
        game_logic.stop_game()

    return HttpResponse('ok')
