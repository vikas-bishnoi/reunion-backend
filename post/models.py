from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(to='main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(to='main.User', related_name='liked', blank=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=256)
    author = models.ForeignKey('main.User', on_delete=models.CASCADE)
