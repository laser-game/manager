from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from .base import BaseModel
from ..conf import core_settings
from ..utils.validators import MinDurationValidator, MaxDurationValidator


class TypeColor(BaseModel):
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.color

    class Meta(object):
        verbose_name = _('Type color')
        verbose_name_plural = _('Types colors')


class Player(BaseModel):
    name = models.CharField(max_length=32)
    email = models.EmailField(blank=True)

    class Meta(object):
        verbose_name = _('Player')
        verbose_name_plural = _('Players')


class Team(BaseModel):
    type_color = models.ForeignKey(TypeColor, related_name='team_type_color', on_delete=models.PROTECT)

    name = models.CharField(max_length=32)

    class Meta(object):
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class TypeGame(BaseModel):
    GAME_MODE = (
        ('S', _('solo')),
        ('T', _('team')),
    )
    BUTTON_ACTION_MODE = (
        ('D', _('disable')),
        ('F', _('fuse')),
        ('W', _('white flashlight')),
        ('U', _('ultra violet flashlight')),
    )
    name = models.CharField(max_length=32)
    game_mode = models.CharField(max_length=1, choices=GAME_MODE)
    button_action_mode = models.CharField(max_length=1, choices=BUTTON_ACTION_MODE)
    game_duration = models.DurationField(
        validators=[
            MinDurationValidator(core_settings.MIN_GAME_DURATION),
            MaxDurationValidator(core_settings.MAX_GAME_DURATION),
        ]
    )
    death_duration = models.DurationField(
        validators=[
            MinDurationValidator(core_settings.MIN_DEATH_DURATION),
            MaxDurationValidator(core_settings.MAX_DEATH_DURATION),
        ]
    )
    batch_shots_count = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(core_settings.MIN_SHOTS_IN_BATCH),
            MaxValueValidator(core_settings.MAX_SHOTS_IN_BATCH),
        ]
    )
    enable_sound = models.BooleanField()
    enable_vest_light = models.BooleanField()
    enable_immorality = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Type game')
        verbose_name_plural = _('Types games')


class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, related_name='game_type_game', on_delete=models.PROTECT)

    GAME_STATE = (
        ('S', _('set')),
        ('P', _('play')),
        ('B', _('break')),
        ('D', _('done')),
    )
    state = models.CharField(max_length=1, choices=GAME_STATE)
    start = models.DateTimeField()

    class Meta(object):
        verbose_name = _('Game')
        verbose_name_plural = _('Games')


class GamePlayer(BaseModel):
    game = models.ForeignKey(Game, related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='game_player_team', null=True, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='game_player_player', on_delete=models.PROTECT)
    type_color = models.ForeignKey(TypeColor, related_name='game_player_type_color', on_delete=models.PROTECT)

    points = models.IntegerField()
    kills_count = models.PositiveSmallIntegerField()
    deaths_count = models.PositiveSmallIntegerField()
    friendly_kills_count = models.PositiveSmallIntegerField()

    class Meta(object):
        verbose_name = _('Game player')


class TypeEvent(BaseModel):
    TYPE_EVENTS = (
        ('K', _('player kill player')),
        ('F', _('friendly fire')),
        ('T', _('trap')),
        ('B', _('bonus')),
    )
    identifier = models.CharField(max_length=1, choices=TYPE_EVENTS)

    class Meta(object):
        verbose_name = _('Type event')
        verbose_name_plural = _('Types events')


class Event(BaseModel):
    game = models.ForeignKey(Game, related_name='event_game', on_delete=models.PROTECT)
    type_event = models.ForeignKey(TypeEvent, related_name='event_type_event', on_delete=models.PROTECT)

    time = models.DurationField()

    @property
    def time_occurred(self):
        return self.game.start + self.time

    class Meta(object):
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
