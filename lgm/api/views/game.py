from django.http import HttpResponse
from django.views import View
import json

from core import game_logic


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
