from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from reconnectapi.models import Post


class PostView(ViewSet):
    """Reconnect Comment View"""

    def retrieve(self, request, pk):
        """retrieve comment"""
        comment = Post.objects.get(pk=pk)
        serializer = PostSerializer(comment)
        return Response(serializer.data)
    
    def create(self, request):

        author = User.objects.get(pk=request.data["user"])

        post = Post.objects.create(
        content=request.data["content"],
        author = author
        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):

        author = User.objects.get(pk=request.data["user"])

        post = Post.objects.get(pk=pk)
        post.content = request.data["content"]
        author = author
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

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