from django.contrib import admin
from .models import Post, Category, Comments

# Register your models here.
admin.site.register([Post, Category,Comments])
