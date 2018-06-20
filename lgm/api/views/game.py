from django.http import HttpResponse
import json


def game_config(request):
    if request.method == "POST" and request.is_ajax():
        config = json.loads(request.body)
        print(config['SetGame'])

        print('OK')
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
