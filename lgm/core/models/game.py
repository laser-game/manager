from django.db import models
from .base import BaseModel


class Player(BaseModel):
    pass


class Team(BaseModel):
    pass


class TypeGame(BaseModel):
    pass


class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, on_delete=models.PROTECT)


class GamePlayer(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)


class TypeAction(BaseModel):
    pass


class Action(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    type_action = models.ForeignKey(TypeAction, on_delete==models.PROTECT)
