from rest_framework import serializers
from api.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "city", "postal_code", "gender", "uuid")
