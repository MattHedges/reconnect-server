from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    since = models.DateField(auto_now_add=True)