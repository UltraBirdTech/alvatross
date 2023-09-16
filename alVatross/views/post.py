from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.post import Post

@login_required
def index(request):
    params = {}
    post_list = Post.objects.all()
    params['post_list'] = post_list
    return render(request, 'alVatross/post.html', params)

def insert(request):
    pass

def update(request):
    pass

def delete(request):
    pass
