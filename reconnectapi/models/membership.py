from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
