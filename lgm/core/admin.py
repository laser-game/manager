from django.contrib import admin

from .models import TypeGame


@admin.register(TypeGame)
class TypeGameAdmin(admin.ModelAdmin):
    pass
