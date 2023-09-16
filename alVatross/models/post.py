from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    status = models.CharField(max_length=10) # active/delete 
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 外部キー
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
