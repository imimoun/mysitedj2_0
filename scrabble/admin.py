# coding: utf-8
from django.contrib import admin

from scrabble.models.Deck import Deck
from scrabble.models.Game import Game
from scrabble.models.Player import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("ID_player", "name", )
    ordering = ("ID_player", "name", )


class DeckAdmin(admin.ModelAdmin):
    list_display = ("ID_token", "ID_deck", "token", )
    ordering = ("ID_token", "ID_deck", "token", )
    search_fields = ("ID_deck", "token", )


class GameAdmin(admin.ModelAdmin):
    list_display = ("ID_game", "Deck", "Player_1", "Player_2", "Hand_player_1", "Hand_player_2", "GameBoard", )
    ordering = ("ID_game", "Deck", "Player_1", "Player_2", "Hand_player_1", "Hand_player_2", "GameBoard", )
    search_fields = ("Player_1", "Player_2", )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Deck, DeckAdmin)
admin.site.register(Game, GameAdmin)
