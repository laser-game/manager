from django.contrib import admin
from django.utils.html import format_html

from core.models import (
    Event,
    Game,
    GamePlayer,
    Player,
    Switch,
    Team,
    TypeColor,
    TypeEvent,
    TypeGame,
    TypeGameSwitch,
    TypeSwitch,
    Vest,
)


@admin.register(Vest)
class TypeGameAdmin(admin.ModelAdmin):
    list_display = (
        'index',
        'state',
        'enable',
        'online',
        'battery',
    )


@admin.register(TypeSwitch)
class TypeSwitchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'index',
        'enable',
    )


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = (
        'type_switch',
        'event',
        'time_on',
        #'type_switch__enable',
    )


class TypeGameSwitchInline(admin.TabularInline):
    model = TypeGameSwitch


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
    inlines = [TypeGameSwitchInline]


@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    list_display = ('identifier',)


@admin.register(TypeColor)
class TypeColorAdmin(admin.ModelAdmin):
    @staticmethod
    def color_display(obj: TypeColor):
        return format_html("""
            <svg viewBox="0 -7 90 107" style="height: 1em; fill: {};">
                <polygon points="0,0 90,0 85,80 45,100 5,80"/>
            </svg>""",
            obj.css
        )

    list_display = ('name', 'index', 'hw', 'css', 'color_display')


class GamePlayerInline(admin.TabularInline):
    model = GamePlayer


class EventInline(admin.TabularInline):
    model = Event


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GamePlayerInline, EventInline]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [GamePlayerInline]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
