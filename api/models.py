# coding: utf-8
import uuid

from django.db import models


class UUIDModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Client(UUIDModel):
    first_name = models.CharField(verbose_name='Prénom', max_length=255)
    last_name = models.CharField(verbose_name='Nom', max_length=255)
    city = models.CharField(verbose_name='Ville', max_length=255)
    postal_code = models.CharField(verbose_name='Code postal', max_length=255)
    gender = models.CharField(verbose_name='Civilite', max_length=255)
