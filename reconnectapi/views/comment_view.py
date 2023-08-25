from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from reconnectapi.models import Comment, Post
from django.contrib.auth.models import User


class CommentView(ViewSet):
    """Reconnect Comment View"""

    def retrieve(self, request, pk):
        """retrieve comment"""
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def create(self, request):
        """create comment"""
        user = User.objects.get(pk=request.data["user"])
        post = Post.objects.get(pk=request.data["post"])
        

        comment = Comment.objects.create(
        comment=request.data["comment"],
        timestamp=request.data["timestamp"],
        user=user,
        post=post
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """update Comment"""
        user = User.objects.get(pk=request.data["user"])
        post = Post.objects.get(pk=request.data["post"])

        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        comment.timestamp = request.data["timestamp"]
        user = user
        post = post
        
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comment
    """
    class Meta:
        model = Comment
        fields = ('id', 'content', 'timestamp', 'user', 'post' )
        depth = 1