from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class Vest(BaseModel):
    MODE = (
        ('O', _('ok')),
        ('B', _('break wire')),
    )
    index = models.PositiveSmallIntegerField(_('Index of vest'))
    address = models.PositiveSmallIntegerField(_('Address of vest'))
    battery = models.PositiveSmallIntegerField(_('Battery'))
    enable = models.BooleanField(_('Enable vest'))
    online = models.BooleanField(_('Online vest'))
    mode = models.CharField(_('State'), max_length=1, choices=MODE)

    def __str__(self):
        return str(self.index)

    class Meta(object):
        verbose_name = _('Vest')
        verbose_name_plural = _('Vests')
