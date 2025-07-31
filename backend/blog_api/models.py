from django.db import models

class Blog(models.Model):
    user_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    tag = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
