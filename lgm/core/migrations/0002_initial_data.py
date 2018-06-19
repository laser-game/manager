from datetime import timedelta

from django.db import migrations
from django.db.migrations import RunPython

from core.conf import core_settings
from core.models import TypeColor, TypeEvent, TypeGame, TypeSwitch, Vest


def insert_type_colors(schema, apps):
    for color in core_settings.DEFAULT_COLORS:
        type_color = TypeColor()
        type_color.name = color['name']
        type_color.index = color['index']
        type_color.css = color['css']
        type_color.hw = color['hw']
        type_color.save()


def insert_type_event(schema, apps):
    for event in TypeEvent.TYPE_EVENTS:
        type_event = TypeEvent()
        type_event.identifier = event[0]
        type_event.save()


def insert_type_game(schema, apps):
    type_game = TypeGame()
    type_game.name = 'Solo'
    type_game.game_mode = 'S'
    type_game.button_action_mode = 'F'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = True
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'Team Game'
    type_game.game_mode = 'T'
    type_game.button_action_mode = 'F'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = True
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'Invisible'
    type_game.game_mode = 'S'
    type_game.button_action_mode = 'F'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'Invisible Team'
    type_game.game_mode = 'T'
    type_game.button_action_mode = 'F'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'S.W.A.T. - Light'
    type_game.game_mode = 'S'
    type_game.button_action_mode = 'W'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'S.W.A.T. - Light Team'
    type_game.game_mode = 'T'
    type_game.button_action_mode = 'W'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'S.W.A.T. - UV'
    type_game.game_mode = 'S'
    type_game.button_action_mode = 'U'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()

    type_game = TypeGame()
    type_game.name = 'S.W.A.T. - UV Team'
    type_game.game_mode = 'T'
    type_game.button_action_mode = 'U'
    type_game.sound_set_type = 'CZ'
    type_game.game_duration = timedelta(seconds=15 * 60)
    type_game.death_duration = timedelta(seconds=5)
    type_game.batch_shots_count = 1
    type_game.enable_sound = True
    type_game.enable_vest_light = False
    type_game.enable_immorality = False
    type_game.save()


def insert_type_switch(schema, apps):
    for i in range(16):
        type_switch = TypeSwitch()
        type_switch.name = 'SWITCH {:02d}'.format(i)
        type_switch.index = i
        type_switch.enable = True
        type_switch.save()


def insert_vest(schema, apps):
    for i in range(16):
        vest = Vest()
        vest.address = i
        vest.battery = 0
        vest.enable = True
        vest.online = False
        vest.has_failure = False
        vest.save()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        RunPython(insert_type_switch),
        RunPython(insert_type_colors),
        RunPython(insert_type_event),
        RunPython(insert_type_game),
        RunPython(insert_vest),
    ]
