from django.http import HttpResponse
from django.shortcuts import render

from core.conf import core_settings


def settings(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }

    return render(request, 'web/settings/index.html', context)


def stream(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/stream/index.html', context)


def archive(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': core_settings.DEFAULT_TEAM_NAMES,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/archive/index.html', context)
