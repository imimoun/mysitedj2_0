# coding: utf-8
import uuid

from django.db import models


def get_uuid():
    """Return an uuid without hyphen."""
    return str(uuid.uuid4().hex)


class UUIDModel(models.Model):
    uuid = models.CharField(unique=True, max_length=32, default=get_uuid, editable=False)

    class Meta:
        abstract = True


class Client(UUIDModel):
    id = models.AutoField(primary_key=True, default=None)
    first_name = models.CharField(verbose_name='Prénom', max_length=255)
    last_name = models.CharField(verbose_name='Nom', max_length=255)
    city = models.CharField(verbose_name='Ville', max_length=255)
    postal_code = models.CharField(verbose_name='Code postal', max_length=255)
    gender = models.CharField(verbose_name='Civilite', max_length=255)
