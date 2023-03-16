from django.db import models
from django.utils import timezone

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    author = models.ForeignKey('main.User', on_delete=models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(to='main.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    comments = models.ManyToManyField("post.Comment", related_name="comments", blank=True)