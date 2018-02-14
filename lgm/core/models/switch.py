from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class TypeSwitch(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    index = models.PositiveSmallIntegerField(_('Index of switch'))
    enable = models.BooleanField(_('Enable switch'))

    class Meta(object):
        verbose_name = _('Type switch')
        verbose_name_plural = _('Type switches')

class Switch(BaseModel):
    type_switch = models.ForeignKey('core.TypeSwitch', related_name='switch_type_switch', on_delete=models.PROTECT)

    SWITCH_EVENT = (
        ('D', _('disable')),
        ('C', _('after configuration')),
        ('S', _('after start')),
        ('E', _('after end')),
    )
    time_on = models.DateTimeField(_('Time of switch'))
    switch_event = models.CharField(_('Switch event'), max_length=1, choices=SWITCH_EVENT)

    def __str__(self):
        return self.type_switch.name

    class Meta(object):
        verbose_name = _('Switch')
        verbose_name_plural = _('switches')
