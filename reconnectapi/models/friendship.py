from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    since = models.DateField(auto_now_add=True)