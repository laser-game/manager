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


class Player(BaseModel):
    name = models.CharField(_('Name'), max_length=32)
    email = models.EmailField(_('Email for registered players'), blank=True)

    class Meta(object):
        verbose_name = _('Player')
        verbose_name_plural = _('Players')


class Team(BaseModel):
    type_color = models.ForeignKey(TypeColor, related_name='team_type_color', on_delete=models.PROTECT)

    name = models.CharField(_('Name'), max_length=32)

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
    name = models.CharField(_('Name'), max_length=32)
    game_mode = models.CharField(_('Game mode'), max_length=1, choices=GAME_MODE)
    button_action_mode = models.CharField(_('Mode of button action'), max_length=1, choices=BUTTON_ACTION_MODE)
    game_duration = models.DurationField(
        _('Time duration of game'),
        validators=[
            MinDurationValidator(core_settings.MIN_GAME_DURATION),
            MaxDurationValidator(core_settings.MAX_GAME_DURATION),
        ]
    )
    death_duration = models.DurationField(
        _('Time duration of death state'),
        validators=[
            MinDurationValidator(core_settings.MIN_DEATH_DURATION),
            MaxDurationValidator(core_settings.MAX_DEATH_DURATION),
        ]
    )
    batch_shots_count = models.PositiveSmallIntegerField(
        _('Count of shots in batch'),
        validators=[
            MinValueValidator(core_settings.MIN_SHOTS_IN_BATCH),
            MaxValueValidator(core_settings.MAX_SHOTS_IN_BATCH),
        ]
    )
    enable_sound = models.BooleanField(_('Enable sound'))
    enable_vest_light = models.BooleanField(_('Enable vest light'))
    enable_immorality = models.BooleanField(_('Enable immorality'))

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
    state = models.CharField(_('State of game'), max_length=1, choices=GAME_STATE)
    start = models.DateTimeField(_('Start of game'))

    class Meta(object):
        verbose_name = _('Game')
        verbose_name_plural = _('Games')


class GamePlayer(BaseModel):
    game = models.ForeignKey(Game, related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='game_player_team', null=True, blank=True, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='game_player_player', on_delete=models.PROTECT)
    type_color = models.ForeignKey(TypeColor, related_name='game_player_type_color', on_delete=models.PROTECT)

    points = models.IntegerField(_('Total points'))
    kills_count = models.PositiveSmallIntegerField(_('Count of kills'))
    deaths_count = models.PositiveSmallIntegerField(_('Count of deaths'))
    friendly_kills_count = models.PositiveSmallIntegerField(_('Count of friendly kills'))

    class Meta(object):
        verbose_name = _('Game player')


class TypeEvent(BaseModel):
    TYPE_EVENTS = (
        ('K', _('player kill player')),
        ('F', _('friendly fire')),
        ('T', _('trap')),
        ('B', _('bonus')),
    )
    TYPE_EVENTS_MAPPING = dict(TYPE_EVENTS)
    identifier = models.CharField(_('Identifier'), max_length=1, choices=TYPE_EVENTS)

    class Meta(object):
        verbose_name = _('Type event')
        verbose_name_plural = _('Types events')

    def __str__(self):
        return self.TYPE_EVENTS_MAPPING.get(self.identifier)


class Event(BaseModel):
    game = models.ForeignKey(Game, related_name='event_game', on_delete=models.PROTECT)
    type_event = models.ForeignKey(TypeEvent, related_name='event_type_event', on_delete=models.PROTECT)

    time = models.DurationField(_('Time elapsed from start of game'))

    @property
    def time_occurred(self):
        return self.game.start + self.time

    class Meta(object):
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
