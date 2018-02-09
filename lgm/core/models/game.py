from django.db import models
from .base import BaseModel


class TypeAction(BaseModel):
    pass


class Action(BaseModel):
    type_action = models.ForeignKey(TypeAction, on_delete=models.PROTECT)


class Player(BaseModel):
    pass


class Team(BaseModel):
    pass


class GamePlayer(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    game_player = models.ForeignKey(GamePlayer, on_delete=models.PROTECT)


class TypeGame(BaseModel):
    pass


class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    game_player = models.ForeignKey(GamePlayer, on_delete=models.PROTECT)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)
