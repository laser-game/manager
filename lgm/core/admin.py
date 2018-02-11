from django.contrib import admin

from core.models.game import TypeEvent, TypeColor, Game, Player, Team, GamePlayer
from .models import TypeGame


@admin.register(TypeGame)
class TypeGameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'game_mode',
        'button_action_mode',
        'game_duration',
        'death_duration',
        'enable_vest_light',
        'enable_immorality',
        'enable_sound',
    )


@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    list_display = ('identifier',)


@admin.register(TypeColor)
class TypeColorAdmin(admin.ModelAdmin):
    list_display = ('color',)


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
