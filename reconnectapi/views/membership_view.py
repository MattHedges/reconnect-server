from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reconnectapi.models import Membership, Group
from django.contrib.auth.models import User



class MembershipView(ViewSet):
    
    def create(self, request):

        user = User.objects.get(pk=request.data["user"])
        group = Group.objects.get(pk=request.data["group"])

        membership = Membership.objects.create(
        user = user,
        group = group,
        date_joined=request.data["date_joined"]
        )
        serializer = MembershipSerializer(membership)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        membership = Membership.objects.get(pk=pk)
        serializer = MembershipSerializer(membership)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        membership = Membership.objects.get(pk=pk)
        membership.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class MembershipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membership
        fields = ('id', 'user', 'group', 'date_joined' )
