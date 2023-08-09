from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reconnectapi.models import Topic
from rest_framework.decorators import action


class TopicView(ViewSet):
    """Level up topic view"""

    def retrieve(self, request, pk):
        topic = Topic.objects.get(pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def create(self, request):

        topic = Topic.objects.create(
        name=request.data["name"]
        )
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        topic = Topic.objects.get(pk=pk)
        topic.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TopicSerializer(serializers.ModelSerializer):
    """JSON serializer for topic
    """
    class Meta:
        model = Topic
        fields = ('id', 'name' )
        depth = 1