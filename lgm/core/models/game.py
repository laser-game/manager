from django.db import models
from .base import BaseModel


class Player(BaseModel):
    name = models.CharField(max_length=32)
    email = models.EmailField(blank=True)

class Team(BaseModel):
    name = models.CharField(max_length=32)


class TypeGame(BaseModel):
    pass


class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, related_name='game_type_game', on_delete=models.PROTECT)

    GAME_STATE = (
        ('S', 'set'),
        ('P', 'play'),
        ('D', 'done'),
    )
    state = models.CharField(max_length=1, choices=GAME_STATE)


class GamePlayer(BaseModel):
    game = models.ForeignKey(Game, related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='game_player_team', null=True, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='game_player_player', on_delete=models.PROTECT)

    points = models.IntegerField()
    kills_count = models.PositiveSmallIntegerField()
    deaths_count = models.PositiveSmallIntegerField()
    friendly_kills_count = models.PositiveSmallIntegerField()


class TypeAction(BaseModel):
    TYPE_ACTION = (
        ('K', 'player kill player'),
        ('F', 'friendly_fire'),
        ('T', 'trap'),
        ('B', 'bonus'),
    )
    act = models.CharField(max_length=1, choices=TYPE_ACTION)


class Action(BaseModel):
    game = models.ForeignKey(Game, related_name='action_game', on_delete=models.PROTECT)
    type_action = models.ForeignKey(TypeAction, related_name='action_type_action', on_delete=models.PROTECT)

    time = models.CharField(max_length=8)
