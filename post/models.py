from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(to='main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(to='main.User', related_name='likes', blank=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post')
    comment = models.CharField(max_length=256)
    author = models.ForeignKey('main.User', on_delete=models.CASCADE)
