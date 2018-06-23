from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from ..conf import core_settings
from ..utils.validators import MaxDurationValidator, MinDurationValidator
from .base import BaseModel


class TypeGame(BaseModel):
    GAME_MODE_SOLO = 'S'
    GAME_MODE_TEAM = 'T'
    GAME_MODE = (
        (GAME_MODE_SOLO, _('solo')),
        (GAME_MODE_TEAM, _('team')),
    )

    BUTTON_ACTION_DISABLE = 'D'
    BUTTON_ACTION_FUSE = 'F'
    BUTTON_ACTION_FLASHLIGHT_WH = 'W'
    BUTTON_ACTION_FLASHLIGHT_UV = 'U'
    BUTTON_ACTION_MODE = (
        (BUTTON_ACTION_DISABLE, _('disable')),
        (BUTTON_ACTION_FUSE, _('fuse')),
        (BUTTON_ACTION_FLASHLIGHT_WH, _('white flashlight')),
        (BUTTON_ACTION_FLASHLIGHT_UV, _('ultra violet flashlight')),
    )

    SOUND_SET_TYPE_CZ = 'CZ'
    SOUND_SET_TYPE_EN = 'EN'
    SOUND_SET_TYPE = (
        (SOUND_SET_TYPE_CZ, _('czech')),
        (SOUND_SET_TYPE_EN, _('english')),
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


class Game(TypeGame):
    STATE_SET = 'S'
    STATE_PLAY = 'P'
    STATE_BREAK = 'B'
    STATE_DONE = 'D'

    GAME_STATE = (
        (STATE_SET, _('set')),
        (STATE_PLAY, _('play')),
        (STATE_BREAK, _('break')),
        (STATE_DONE, _('done')),
    )

    state = models.CharField(_('State of game'), max_length=1, choices=GAME_STATE)
    created_time = models.DateTimeField(_('Created time'))
    started_time = models.DateTimeField(_('Started time'), null=True, blank=True)
    elapsed_time = models.DurationField(_('Elapsed time'), null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + str(self.created_time)

    class Meta(object):
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
