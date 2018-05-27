from django.contrib.postgres.fields import ArrayField
from django.db import models

from scrabble.models.Token import Token


class Game(models.Model):
    ID_game = models.AutoField(primary_key=True)
    Deck = models.ForeignKey(
        'Deck',
        on_delete=models.CASCADE,
    )
    Player_1 = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    Player_2 = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related"
    )
    Hand_player_1 = ArrayField(
        models.CharField(max_length=7, choices=Token.choices()),
        size=7,
    )
    Hand_player_2 = ArrayField(
        models.CharField(max_length=7, choices=Token.choices()),
        size=7,
    )
    GameBoard = ArrayField(
        ArrayField(
            models.CharField(max_length=7, choices=Token.choices()),
            size=15,
        ),
        size=15,
    )
