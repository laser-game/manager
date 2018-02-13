from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class TypeColor(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    hw = models.CharField(_('RGB code for HW'), max_length=7)
    css = models.CharField(_('RGB code for CSS'), max_length=7)
    index = models.PositiveSmallIntegerField(_('Index of color'))


    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Type color')
        verbose_name_plural = _('Types colors')
