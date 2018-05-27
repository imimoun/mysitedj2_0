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
    )
    Hand_player_1 = models.ArrayField(
        models.CharField(choices=[(tag, tag.value) for tag in Token]),
        size=7,
    )
    Hand_player_2 = models.ArrayField(
        models.CharField(choices=[(tag, tag.value) for tag in Token]),
        size=7,
    )
    name = models.CharField(max_length=100)
    GameBoard = models.ArrayField(
        models.ArrayField(
            models.CharField(choices=[(tag, tag.value) for tag in Token]),
            size=15,
        ),
        size=15,
    )
