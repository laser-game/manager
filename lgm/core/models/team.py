from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class Team(BaseModel):
    type_color = models.ForeignKey('core.TypeColor', related_name='team_type_color', on_delete=models.PROTECT)

    name = models.CharField(_('Name'), max_length=32)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
