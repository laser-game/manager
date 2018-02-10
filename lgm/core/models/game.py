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
    type_game = models.ForeignKey(TypeGame, on_delete=models.PROTECT)


class GamePlayer(BaseModel):
    kill = models.IntegerField()
    death = models.IntegerField()
    score = models.IntegerField()
    friendly_fire = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)


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
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    type_action = models.ForeignKey(TypeAction, on_delete=models.PROTECT)
