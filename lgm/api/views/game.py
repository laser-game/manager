from django.http import HttpResponse
import json


def game_config(request):
    if request.method == "POST" and request.is_ajax():
        config = json.loads(request.body)

        for i in config:
            print('\n======================\n', i, '\n======================')
            for j in config[i]:
                try:
                    print(j, config[i][j])
                except:
                    print(j)

        print('OK')
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
