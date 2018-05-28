from django.db import models


class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
