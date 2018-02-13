from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class Team(BaseModel):
    type_color = models.ForeignKey('core.TypeColor', related_name='team_type_color', on_delete=models.PROTECT)

    name = models.CharField(_('Name'), max_length=32)

    class Meta(object):
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
