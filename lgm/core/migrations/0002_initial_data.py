from datetime import timedelta

from django.db import migrations
from django.db.migrations import RunPython

from core.conf import core_settings
from core.models import TypeColor, TypeEvent, TypeGame, TypeSwitch, Vest


def insert_type_colors(schema, apps):
    type_color = TypeColor()
    type_color.index = 0
    type_color.name = 'red'
    type_color.css = '#FF0000'
    type_color.hw = '#FF0000'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 1
    type_color.name = 'orange'
    type_color.css = '#FFA500'
    type_color.hw = '#FFA500'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 2
    type_color.name = 'yellow'
    type_color.css = '#FFFF00'
    type_color.hw = '#FFFF00'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 3
    type_color.name = 'green'
    type_color.css = '#00FF00'
    type_color.hw = '#00FF00'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 4
    type_color.name = 'aqua'
    type_color.css = '#00FFFF'
    type_color.hw = '#00FFFF'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 5
    type_color.name = 'blue'
    type_color.css = '#0000FF'
    type_color.hw = '#0000FF'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 6
    type_color.name = 'purple'
    type_color.css = '#FF00FF'
    type_color.hw = '#FF00FF'
    type_color.save()

    type_color = TypeColor()
    type_color.index = 7
    type_color.name = 'pink'
    type_color.css = '#FFC0CB'
    type_color.hw = '#FFC0CB'
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    type_game.game_duration = timedelta(minutes=15)
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
    for i in range(core_settings.MIN_PLAYERS, core_settings.MAX_PLAYERS + 1):
        vest = Vest()
        vest.address = i
        vest.battery = 0
        vest.enable = True
        vest.online = True
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
