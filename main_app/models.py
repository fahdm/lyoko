from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='post')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255,default='ninja')
   

    def __str__(self):
        return f"{self.title} | {self.author.username}"
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name= "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)

