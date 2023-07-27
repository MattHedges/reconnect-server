from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

    description = models.CharField(max_length=50)