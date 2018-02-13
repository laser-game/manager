from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class TypeColor(BaseModel):
    color = models.CharField(_('RGB code'), max_length=7)

    def __str__(self):
        return self.color

    class Meta(object):
        verbose_name = _('Type color')
        verbose_name_plural = _('Types colors')
