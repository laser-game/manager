from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

from core.conf import core_settings


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
