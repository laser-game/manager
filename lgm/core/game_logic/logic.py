from django.utils import timezone
from datetime import timedelta

from ..models import (
    TypeColor,
    Game,
    TypeGame,
    GamePlayer,
    GameTeam,
    Player, Team,
    Vest
)


def start_game():
    dat_game = Game.objects.filter(state=Game.STATE_SET).order_by('-started_time')
    if not dat_game.exists() or Game.objects.filter(state=Game.STATE_PLAY).exists():
        return 'error'

    dat_game = dat_game.first()
    dat_game.state = Game.STATE_PLAY
    dat_game.started_time = timezone.now()
    dat_game.save()
    return 'ok'


def stop_game():
    dat_game = Game.objects.filter(state=Game.STATE_PLAY).order_by('-started_time')
    if not dat_game.exists():
        return 'error'

    dat_game = dat_game.first()
    dat_game.state = Game.STATE_BREAK
    dat_game.save()
    return 'ok'
