from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class TypeEvent(BaseModel):
    TYPE_EVENTS = (
        ('K', _('player kill player')),
        ('F', _('friendly fire')),
        ('T', _('trap')),
        ('B', _('bonus')),
    )
    TYPE_EVENTS_MAPPING = dict(TYPE_EVENTS)
    identifier = models.CharField(_('Identifier'), max_length=1, choices=TYPE_EVENTS)

    class Meta(object):
        verbose_name = _('Type event')
        verbose_name_plural = _('Types events')

    def __str__(self):
        return self.TYPE_EVENTS_MAPPING.get(self.identifier)


class Event(BaseModel):
    game = models.ForeignKey('core.Game', related_name='event_game', on_delete=models.PROTECT)
    type_event = models.ForeignKey('core.TypeEvent', related_name='event_type_event', on_delete=models.PROTECT)

    time = models.DurationField(_('Time elapsed from start of game'))

    @property
    def time_occurred(self):
        return self.game.start + self.time

    class Meta(object):
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
