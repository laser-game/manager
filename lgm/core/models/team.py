from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from .game import GameEntityBaseModel


class Team(BaseModel):
    name = models.CharField(_('Name'), max_length=32)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class GameTeam(GameEntityBaseModel):
    game = models.ForeignKey(
        'core.Game',
        related_name='game_team_game',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    type_color = models.ForeignKey(
        'core.TypeColor',
        related_name='game_team_type_color',
        on_delete=models.PROTECT
    )
    team = models.ForeignKey(
        'core.Team',
        related_name='game_team_team',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.team.name

    class Meta(object):
        verbose_name = _('Game team')
