from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    description = models.CharField(max_length=50)