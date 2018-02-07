from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from core.conf import core_settings

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def settings(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAME': core_settings.DEFAULT_TEAM_NAME,
        'COLOR': core_settings.COLOR,
    }

    return render(request, 'web/settings/index.html', context)

def stream(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAME': core_settings.DEFAULT_TEAM_NAME,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/stream/index.html', context)

def archive(request):
    context = {
        'MAX_PLAYERS': core_settings.MAX_PLAYERS,
        'DEFAULT_TEAM_NAME': core_settings.DEFAULT_TEAM_NAME,
        'COLOR': core_settings.COLOR,
    }
    return render(request, 'web/archive/index.html', context)
