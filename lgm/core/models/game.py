from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from ..conf import core_settings
from ..utils.validators import MaxDurationValidator, MinDurationValidator
from .base import BaseModel


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
    SOUND_SET_TYPE = (
        ('CZ', _('czech')),
        ('EN', _('english')),
    )
    name = models.CharField(_('Name'), max_length=32)
    game_mode = models.CharField(_('Game mode'), max_length=1, choices=GAME_MODE)
    button_action_mode = models.CharField(_('Mode of button action'), max_length=1, choices=BUTTON_ACTION_MODE)
    sound_set_type = models.CharField(_('Set of sounds'), max_length=1, choices=SOUND_SET_TYPE)
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
    type_game = models.ForeignKey('core.TypeGame', related_name='game_type_game', on_delete=models.PROTECT)

    GAME_STATE = (
        ('S', _('set')),
        ('P', _('play')),
        ('B', _('break')),
        ('D', _('done')),
    )
    state = models.CharField(_('State of game'), max_length=1, choices=GAME_STATE)
    start = models.DateTimeField(_('Start of game'))

    def __str__(self):
        return self.type_game.name + ' ' + str(self.start)

    class Meta(object):
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
