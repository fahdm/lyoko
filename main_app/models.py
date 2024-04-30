from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} | {self.author.username}"