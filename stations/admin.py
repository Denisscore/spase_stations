
from django.contrib import admin
from .models import Station, Indication


@admin.register(Station)
class GenreAdmin(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(Indication)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('user',)
