from django.http import HttpResponse


def game_config(request):
    if request.method == "POST" and request.is_ajax():
        for key in request.POST:
            print(key)
            value = request.POST[key]
            print(value)

        print('OK')
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
