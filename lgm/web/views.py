from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def settings_game_types(request):
    fr = open('lgm/web/game-types.json')
    data = fr.readlines()
    fr.close()
    return HttpResponse(data)

def settings(request):
    MAX_PLAYERS = 16
    DEFAULT_TEAM_NAMES = (
        "Red team",
        "Orange team",
        "Yellow team",
        "Green team",
        "Aqua team",
        "Blue team",
        "Purple team",
        "Pink team"
    )

    COLOR = (
        "#000000",  # black
        "#FF0000",  # red
        "#FFA500",  # orange
        "#FFFF00",  # yellow
        "#00FF00",  # green
        "#00FFFF",  # aqua
        "#0000FF",  # blue
        "#FF00FF",  # purple
        "#FFC0CB",  # pink
    )

    context = {
        'MAX_PLAYERS': MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': DEFAULT_TEAM_NAMES,
        'COLOR': COLOR,
    }

    return render(request, 'web/settings/index.html', context)

def stream(request):
    MAX_PLAYERS = 16
    DEFAULT_TEAM_NAMES = (
        "Red team",
        "Orange team",
        "Yellow team",
        "Green team",
        "Aqua team",
        "Blue team",
        "Purple team",
        "Pink team"
    )

    COLOR = (
        "#000000",  # black
        "#FF0000",  # red
        "#FFA500",  # orange
        "#FFFF00",  # yellow
        "#00FF00",  # green
        "#00FFFF",  # aqua
        "#0000FF",  # blue
        "#FF00FF",  # purple
        "#FFC0CB",  # pink
    )

    context = {
        'MAX_PLAYERS': MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': DEFAULT_TEAM_NAMES,
        'COLOR': COLOR,
    }

    return render(request, 'web/stream/index.html', context)

def archive(request):
    MAX_PLAYERS = 16
    DEFAULT_TEAM_NAMES = (
        "Red team",
        "Orange team",
        "Yellow team",
        "Green team",
        "Aqua team",
        "Blue team",
        "Purple team",
        "Pink team"
    )

    COLOR = (
        "#000000",  # black
        "#FF0000",  # red
        "#FFA500",  # orange
        "#FFFF00",  # yellow
        "#00FF00",  # green
        "#00FFFF",  # aqua
        "#0000FF",  # blue
        "#FF00FF",  # purple
        "#FFC0CB",  # pink
    )

    context = {
        'MAX_PLAYERS': MAX_PLAYERS,
        'DEFAULT_TEAM_NAMES': DEFAULT_TEAM_NAMES,
        'COLOR': COLOR,
    }

    return render(request, 'web/archive/index.html', context)
