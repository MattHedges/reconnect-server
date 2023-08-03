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

    