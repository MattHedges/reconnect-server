from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from reconnectapi.models import Comment, Post
from django.contrib.auth.models import User


class PostView(ViewSet):
    """Reconnect Comment View"""

    def retrieve(self, request, pk):
        """retrieve comment"""
        comment = Post.objects.get(pk=pk)
        serializer = PostSerializer(comment)
        return Response(serializer.data)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for comment
    """
    class Meta:
        model = Post
        fields = ('id', 'content', 'author' )
        depth = 1