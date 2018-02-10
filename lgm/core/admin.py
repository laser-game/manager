from django.contrib import admin

from core.models.game import TypeEvent, TypeColor, Game, Player, Team, GamePlayer
from .models import TypeGame


@admin.register(TypeGame)
class TypeGameAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeColor)
class TypeColorAdmin(admin.ModelAdmin):
    pass


class GamePlayerInline(admin.TabularInline):
    model = GamePlayer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GamePlayerInline]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [GamePlayerInline]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
