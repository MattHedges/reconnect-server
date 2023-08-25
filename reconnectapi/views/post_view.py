from django.http import HttpResponseServerError, HttpResponse
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

        user = User.objects.get(pk=request.data["user"])

        post = Post.objects.create(
        content=request.data["content"],
        isApproved = request.data["isApproved"],
        user = user
        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])

        post = Post.objects.get(pk=pk)
        post.content = request.data["content"]
        post.isApproved = request.data["isApproved"]
        user = user
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request):
        query_params = request.query_params.dict()

        if 'topic' in query_params:
            posts = Post.objects.filter(topic=query_params['topic'])
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def approve_post(self, post_id):
        post = Post.objects.get(id=post_id)
        post.is_approved = True
        post.save()
    
    def approve_post_view(self, request, post_id):
        if request.user.is_staff:  # Only allow staff users to approve posts
            approve_post(post_id)
            return HttpResponse("Post approved.")
        else:
            return HttpResponse("You do not have permission to approve posts.")

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for comment
    """
    class Meta:
        model = Post
        fields = ('id', 'content', 'user', 'isApproved' )
        depth = 1