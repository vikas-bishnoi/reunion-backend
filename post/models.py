from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(to='main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)