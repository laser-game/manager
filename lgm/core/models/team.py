from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel


class Team(BaseModel):
    name = models.CharField(_('Name'), max_length=32)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class GameTeam(BaseModel):
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

    position = models.PositiveSmallIntegerField(_('Player position'))

    @property
    def team_players(self):
        return self.game.game_player_game.filter(type_color=self.type_color)

    @property
    def points(self):
        return sum(self.team_players.values_list('points', flat=True))

    @property
    def shots_count(self):
        return sum(self.team_players.values_list('shots_count', flat=True))

    @property
    def kills_count(self):
        return sum(self.team_players.values_list('kills_count', flat=True))

    @property
    def deaths_count(self):
        return sum(self.team_players.values_list('deaths_count', flat=True))

    @property
    def friendly_kills_count(self):
        return sum(self.team_players.values_list('friendly_kills_count', flat=True))

    def __str__(self):
        return self.team.name

    class Meta(object):
        verbose_name = _('Game team')
