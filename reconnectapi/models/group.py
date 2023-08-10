from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    members = models.ManyToManyField(User, through='Membership')
    group_creator = models.ForeignKey(User, on_delete=models.CASCADE)