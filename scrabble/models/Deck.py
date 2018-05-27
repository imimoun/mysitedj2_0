from django.db import models

from scrabble.models.Token import Token


class Deck(models.Model):
    ID_token = models.AutoField(primary_key=True)
    ID_deck = models.PositiveIntegerField()
    token = models.CharField(max_length=7, choices=Token.choices())
