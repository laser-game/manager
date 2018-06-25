from django.http import HttpResponse
from django.views import View

from core.game_logic import event


class Kill(View):
    def get(self, request, address1, address2):
        event.kill(address1, address2)
        return HttpResponse('<h1>{}</h1><b>kill</b><h1>{}</h1>'.format(address1, address2))
