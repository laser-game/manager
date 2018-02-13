from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class Player(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    email = models.EmailField(_('Email for registered players'), blank=True)

    class Meta(object):
        verbose_name = _('Player')
        verbose_name_plural = _('Players')


class GamePlayer(BaseModel):
    game = models.ForeignKey('core.Game', related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey('core.Team', related_name='game_player_team', null=True, blank=True, on_delete=models.PROTECT)
    player = models.ForeignKey('core.Player', related_name='game_player_player', on_delete=models.PROTECT)
    type_color = models.ForeignKey('core.TypeColor', related_name='game_player_type_color', on_delete=models.PROTECT)

    points = models.IntegerField(_('Total points'))
    kills_count = models.PositiveSmallIntegerField(_('Count of kills'))
    deaths_count = models.PositiveSmallIntegerField(_('Count of deaths'))
    friendly_kills_count = models.PositiveSmallIntegerField(_('Count of friendly kills'))

    class Meta(object):
        verbose_name = _('Game player')
