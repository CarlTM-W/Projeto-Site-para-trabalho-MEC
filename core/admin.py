from django.contrib import admin
from .models import Noticia, Review, Desconto

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'author', 'category')
    search_fields = ('titulo', 'author', 'category')
    prepopulated_fields = {'slug': ('titulo',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'data', 'author', 'category')
    search_fields = ('name', 'author', 'category')
    prepopulated_fields = {'slug': ('name',)}

class DescontoAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'prazo', 'desc_cat')
    search_fields = ('name', 'desc_cat')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Desconto, DescontoAdmin)