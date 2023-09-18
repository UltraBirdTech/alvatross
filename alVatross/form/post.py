from django import forms
from ..models.post import Post

class AddPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'content', 'status')
