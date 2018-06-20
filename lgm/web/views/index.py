from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from lgba.messages.game import GameStart
from pika.adapters.blocking_connection import BlockingChannel

from core.conf import core_settings
from core.messages.connection import connection

from uuid import uuid4
from django.http import JsonResponse

@login_required
def settings(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/settings/index.html', context)


@login_required
def stream(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/stream/index.html', context)


@login_required
def archive(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/archive/index.html', context)


@login_required
def index(request):
    return redirect(reverse('web:settings'), permanent=True)


class GameStartView(View):
    def get(self, request, *args, **kwargs):
        with connection() as channel:  # type: BlockingChannel
            # TODO: refactor to composite architecture
            channel.queue_declare(queue='commands')

            success = channel.basic_publish(
                exchange='',
                routing_key='commands',
                body=GameStart(uuid4()).serialize()
            )

        return JsonResponse(data=dict(success=success))
