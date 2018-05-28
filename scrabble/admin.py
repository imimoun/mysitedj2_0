# coding: utf-8
from django.contrib import admin

from scrabble.models.Deck import Deck
from scrabble.models.Game import Game
from scrabble.models.Player import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id_player", "name", )
    ordering = ("id_player", "name", )


class DeckAdmin(admin.ModelAdmin):
    list_display = ("id_token", "id_deck", "token", )
    ordering = ("id_token", "id_deck", "token", )
    search_fields = ("id_deck", "token", )


class GameAdmin(admin.ModelAdmin):
    list_display = ("id_game", "id_deck", "player_1", "player_2", "hand_player_1", "hand_player_2", "gameboard", )
    ordering = ("id_game", "id_deck", "player_1", "player_2", "hand_player_1", "hand_player_2", "gameboard", )
    search_fields = ("player_1", "player_2", )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Deck, DeckAdmin)
admin.site.register(Game, GameAdmin)
