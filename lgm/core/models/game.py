from django.db import models
from .base import BaseModel


class Player(BaseModel):
    name = models.CharField(max_length=16)
    mail = models.CharField(max_length=30)

class Team(BaseModel):
    name = models.CharField(max_length=16)
    kill = models.IntegerField()
    death = models.IntegerField()
    score = models.IntegerField()
    friendly_fire = models.IntegerField()


class TypeGame(BaseModel):
    pass


class Game(BaseModel):
    GAME_STATE = (
        ('S', 'set'),
        ('P', 'play'),
        ('D', 'done'),
    )
    state = models.CharField(max_length=1, choices=GAME_STATE)
    type_game = models.ForeignKey(TypeGame, related_name='game_type_game', on_delete=models.PROTECT)


class GamePlayer(BaseModel):
    kill = models.IntegerField()
    death = models.IntegerField()
    score = models.IntegerField()
    friendly_fire = models.IntegerField()
    game = models.ForeignKey(Game, related_name='game_player_game', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='game_player_team', on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='game_player_player', on_delete=models.PROTECT)


class TypeAction(BaseModel):
    TYPE_ACTION = (
        ('K', 'player kill player'),
        ('F', 'friendly_fire'),
        ('T', 'trap'),
        ('B', 'bonus'),
    )
    act = models.CharField(max_length=1, choices=TYPE_ACTION)


class Action(BaseModel):
    time = models.CharField(max_length=8)
    game = models.ForeignKey(Game, related_name='action_game', on_delete=models.PROTECT)
    type_action = models.ForeignKey(TypeAction, related_name='action_type_action', on_delete=models.PROTECT)
