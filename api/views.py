from api.models import Client
from api.serializers import ClientSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ClientList(APIView):
    """List all clients, or add a client."""
    def get(self, request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    """Show, update, or delete a specific client."""
    def get(self, request, uuid):
        client = Client.objects.get(uuid=uuid)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        client = Client.objects.get(uuid=uuid)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        client = Client.objects.get(uuid=uuid)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
