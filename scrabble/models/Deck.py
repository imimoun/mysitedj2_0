from django.db import models

from scrabble.models.Token import Token


class Deck(models.Model):
    id_token = models.AutoField(primary_key=True)
    id_deck = models.PositiveIntegerField(db_index=True)
    token = models.PositiveIntegerField(choices=Token.choices())
