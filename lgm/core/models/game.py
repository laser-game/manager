from django.db import models
from .base import BaseModel

class TypeGame(BaseModel):
    # TODO: JSONField for configuration
    # TODO: see https://github.com/nnseva/django-jsoneditor
    pass

class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, on_delete=models.RESTRICT)
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    game_player = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)
    action = models.ForeignKey(Action, on_delete=models.RESTRICT)

class TypeAction(BaseModel):
    action = models.ForeignKey(Action, on_delete=models.RESTRICT)

class Action(BaseModel):
    pass

class GamePlayer(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)

class Player(BaseModel):
    game_player = models.ForeignKey(GamePlayer, on_delete=models.RESTRICT)

class Team(BaseModel):
    pass
