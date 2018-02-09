from django.db import models
from .base import BaseModel

class TypeGame(BaseModel):
    # TODO: JSONField for configuration
    # TODO: see https://github.com/nnseva/django-jsoneditor
    pass

class Game(BaseModel):
    type_game = models.ForeignKey(TypeGame, on_delete=models.CASCADE)
