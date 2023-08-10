from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from reconnectapi.models import Group


class GroupView(ViewSet):
    """Reconnect group View"""

    def retrieve(self, request, pk):
        """retrieve comment"""
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def create(self, request):
        """create group"""
        member = User.objects.get(pk=request.data["member"])
        group_creator = User.objects.get(pk=request.data["group_creator"])
        

        group = Group.objects.create(
        member=member,
        group_creator=group_creator,
        name=request.data["name"],
        description = request.data["description"]
        )
        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """delete group"""
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GroupSerializer(serializers.ModelSerializer):
    """JSON serializer for comment
    """
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'member', 'group_creator')
        depth = 1