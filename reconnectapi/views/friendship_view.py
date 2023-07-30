from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from reconnectapi.models import Comment, Post, Friendship


class CommentView(ViewSet):
    """Reconnect friendship View"""

    def retrieve(self, request, pk):
        """retrieve comment"""
        friendship = Friendship.objects.get(pk=pk)
        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data)

    def create(self, request):
        """create friendship"""
        user1 = User.objects.get(pk=request.data["user1"])
        user2 = User.objects.get(pk=request.data["user2"])
        

        friendship = Friendship.objects.create(
        user1=user1,
        user2=user2,
        since=request.data["since"]
        )
        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """update friendship"""
        user1 = User.objects.get(pk=request.data["user1"])
        user2 = User.objects.get(pk=request.data["user2"])

        friendship = Friendship.objects.get(pk=pk)
        friendship.since = request.data["since"],
        user1 = user1
        user2 = user2
        friendship.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete friendship"""
        friendship = Friendship.objects.get(pk=pk)
        friendship.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FriendshipSerializer(serializers.ModelSerializer):
    """JSON serializer for comment
    """
    class Meta:
        model = Comment
        fields = ('id', 'user1', 'user2', 'since')
        depth = 1