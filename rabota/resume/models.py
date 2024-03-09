from django.db import models
from django.conf import settings


class Resume(models.Model):
    position = models.CharField(max_length=250)
    name = models.CharField(max_length=350)
    age = models.TextField(max_length=25)
    personality = models.TextField()
    country = models.TextField(max_length=100)
    skills = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
