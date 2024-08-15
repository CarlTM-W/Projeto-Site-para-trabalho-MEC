from django.contrib import admin
from .models import TipoCorreia, Formula

@admin.register(TipoCorreia)
class TipoCorreiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
