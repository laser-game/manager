from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class TypeSwitch(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    index = models.PositiveSmallIntegerField(_('Index of switch'))
    enable = models.BooleanField(_('Enable switch'))

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Type switch')
        verbose_name_plural = _('Type switches')

class TypeGameSwitch(BaseModel):
    switch = models.ForeignKey('core.Switch', related_name='type_game_switch_switch', on_delete=models.PROTECT)
    type_game = models.ForeignKey('core.TypeGame', related_name='type_game_switch_type_game', on_delete=models.PROTECT)

    class Meta(object):
        verbose_name = _('Type Game Switch')
        verbose_name_plural = _('Type Game Switches')

class Switch(BaseModel):
    type_switch = models.ForeignKey('core.TypeSwitch', related_name='switch_type_switch', on_delete=models.PROTECT)

    SWITCH_EVENT = (
        ('D', _('disable')),
        ('C', _('after configuration')),
        ('S', _('after start')),
        ('E', _('after end')),
    )
    time_on = models.DurationField(_('Time of switch'))
    event = models.CharField(_('Switch event'), max_length=1, choices=SWITCH_EVENT)


    class Meta(object):
        verbose_name = _('Switch')
        verbose_name_plural = _('switches')
