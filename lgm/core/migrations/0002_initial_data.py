from core.models.game import TypeGame, TypeColor, TypeEvent
from core.conf import core_settings
from django.db import migrations

def insert_type_colors(schema, apps):
    model = TypeColor()
    for color in core_settings.COLOR:
        model.color = color
        model.save()

def insert_type_event(schema, apps):
    model = TypeEvent()
    for event in TypeEvent.TYPE_EVENTS:
        model.identifier = event[0]
        model.save()

def insert_type_game(schema, apps):
    model = TypeGame()

    model.name = 'Solo'
    model.game_mode = 'S'
    model.button_action_mode = 'F'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = True
    model.enable_immorality = True
    model.save()

    model.name = 'Team Game'
    model.game_mode = 'T'
    model.button_action_mode = 'F'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = True
    model.enable_immorality = True
    model.save()

    model.name = 'Invisible'
    model.game_mode = 'S'
    model.button_action_mode = 'F'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()

    model.name = 'Invisible Team'
    model.game_mode = 'T'
    model.button_action_mode = 'F'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()

    model.name = 'S.W.A.T. - Light'
    model.game_mode = 'S'
    model.button_action_mode = 'W'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()

    model.name = 'S.W.A.T. - Light Team'
    model.game_mode = 'T'
    model.button_action_mode = 'W'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()

    model.name = 'S.W.A.T. - UV'
    model.game_mode = 'S'
    model.button_action_mode = 'W'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()

    model.name = 'S.W.A.T. - UV Team'
    model.game_mode = 'T'
    model.button_action_mode = 'W'
    model.game_duration = 15*60
    model.death_duration = 5
    model.batch_shots_count = 1
    model.enable_sound = True
    model.enable_vest_light = False
    model.enable_immorality = True
    model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
    ]
