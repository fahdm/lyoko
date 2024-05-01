from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='post')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    # created_at = models.DateTimeField()
   

    def __str__(self):
        return f"{self.title} | {self.author.username}"
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))