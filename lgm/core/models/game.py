from django.db import models
from jsonfield import JSONField

from .base import BaseModel


class TypeColor(BaseModel):
    color = models.CharField(max_length=7)


class Player(BaseModel):
    name = models.CharField(max_length=32)
    email = models.EmailField(blank=True)


class Team(BaseModel):
    type_color = models.ForeignKey(TypeColor, related_name='team_type_color', on_delete=models.PROTECT)

    name = models.CharField(max_length=32)


class TypeGame(BaseModel):
    GAME_MODE = (
        ('S', 'solo'),
        ('T', 'team'),
    )
    BUTTON_ACTION_MODE = (
        ('D', 'disable'),
        ('F', 'fuse'),
        ('U', 'ultra violet flashlight'),
        ('W', 'white flashlight'),
    )
    name = models.CharField(max_length=32)
    game_mode = models.CharField(max_length=1, choices=GAME_MODE)
    button_action_mode = models.CharField(max_length=1, choices=BUTTON_ACTION_MODE)
    game_duration = models.DurationField()
    death_duration = models.DurationField()
    enable_immorality = models.BooleanField()
    vest_light_disabled = models.BooleanField()
    enable_sound = models.BooleanField()
    batch_shots_count = models.PositiveSmallIntegerField()


class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, related_name='game_type_game', on_delete=models.PROTECT)

    GAME_STATE = (
        ('S', 'set'),
        ('P', 'play'),
        ('B', 'break'),
        ('D', 'done'),
    )
    state = models.CharField(max_length=1, choices=GAME_STATE)
    start = models.DateTimeField()


class GamePlayer(BaseModel):
    game = models.ForeignKey(Game, related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='game_player_team', null=True, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='game_player_player', on_delete=models.PROTECT)
    type_color = models.ForeignKey(TypeColor, related_name='game_player_type_color', on_delete=models.PROTECT)

    points = models.IntegerField()
    kills_count = models.PositiveSmallIntegerField()
    deaths_count = models.PositiveSmallIntegerField()
    friendly_kills_count = models.PositiveSmallIntegerField()


class TypeEvent(BaseModel):
    TYPE_EVENTS = (
        ('K', 'player kill player'),
        ('F', 'friendly_fire'),
        ('T', 'trap'),
        ('B', 'bonus'),
    )
    identifier = models.CharField(max_length=1, choices=TYPE_EVENTS)


class Event(BaseModel):
    game = models.ForeignKey(Game, related_name='event_game', on_delete=models.PROTECT)
    type_event = models.ForeignKey(TypeEvent, related_name='event_type_event', on_delete=models.PROTECT)

    time = models.DurationField()
