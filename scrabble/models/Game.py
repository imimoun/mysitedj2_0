from django.contrib.postgres.fields import ArrayField
from django.db import models

from scrabble.models.Token import Token


class Game(models.Model):
    id_game = models.AutoField(primary_key=True)
    id_deck = models.PositiveIntegerField()
    player_1 = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    player_2 = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related"
    )
    hand_player_1 = ArrayField(
        models.CharField(max_length=7, choices=Token.choices()),
        size=7,
    )
    hand_player_2 = ArrayField(
        models.CharField(max_length=7, choices=Token.choices()),
        size=7,
    )
    gameboard = ArrayField(
        ArrayField(
            models.CharField(max_length=7, choices=Token.choices()),
            size=15,
        ),
        size=15,
    )
