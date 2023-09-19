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

    def __init__(self, **keywords):
        self.error_messages = []
        super().__init__()

    def __str__(self):
        return self.title

    def clean(self):
        self.clean_title()
        self.clean_content()
        self.clean_status()

    def clean_title(self):
        if len(self.title) > 100:
            self.error_messages.append("タイトルの文字数が100文字を超えています")

    def clean_content(self):
         if len(self.content) > 5000:
            self.error_messages.append("コンテンツの文字数が5000文字を超えています")

    def clean_status(self):
        print('*' * 100)
        print(self.status)
        if not self.status in ['active', 'delete']:
            self.error_messages.append("ステータスに規定外の文字列が入力されています")

       
