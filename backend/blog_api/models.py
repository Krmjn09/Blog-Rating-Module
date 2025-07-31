from django.db import models


class Blog(models.Model):
    user_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
