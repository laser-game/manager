from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class Event(BaseModel):
    TYPE_EVENT_PLAYER_KILL_PLAYER = 'K'
    TYPE_EVENT_FRIENDLY_FIRE = 'F'
    TYPE_EVENT_TRAP = 'T'
    TYPE_EVENT_BONUS = 'B'
    TYPE_EVENTS = (
        (TYPE_EVENT_PLAYER_KILL_PLAYER, _('player kill player')),
        (TYPE_EVENT_FRIENDLY_FIRE, _('friendly fire')),
        (TYPE_EVENT_TRAP, _('trap')),
        (TYPE_EVENT_BONUS, _('bonus')),
    )

    game = models.ForeignKey(
        'core.Game',
        related_name='event_game',
        on_delete=models.PROTECT
    )
    game_player1 = models.ForeignKey(
        'core.GamePlayer',
        related_name='event_game_player1',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    game_player2 = models.ForeignKey(
        'core.GamePlayer',
        related_name='event_game_player2',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    identifier = models.CharField(_('Identifier'), max_length=1, choices=TYPE_EVENTS)
    time = models.DurationField(_('Time elapsed from start of game'))

    @property
    def time_occurred(self):
        return self.game.started_time + self.time

    class Meta(object):
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
