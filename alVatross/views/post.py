from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.post import Post
from ..form.post import AddPostForm

@login_required
def index(request):
    params = {}
    post_list = Post.objects.all()
    print(post_list)
    params['post_list'] = post_list
    return render(request, 'alVatross/post.html', params)

def insert(request):
    params = {
        'add_post_form': AddPostForm(),
        'user': request.user
    }
    if request.method == 'POST':
        params["add_post_form"] = AddPostForm(data=request.POST)
        if params["add_post_form"].is_valid():
            # TODO: Add Validation.
            post = Post(
                title   = request.POST.get("title"),
                content = request.POST.get("content"),
                status  = "active",
                user_id = request.POST.get("user_id"),
            )
            post.save()
            return render(request, 'alVatross/post.html', params)

    return render(request, 'alVatross/insert_post.html', params)

def update(request):
    pass

def delete(request):
    pass
