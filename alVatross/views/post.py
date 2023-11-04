from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from ..models.post import Post
from ..form.post import AddPostForm, EditPostForm

@login_required
def index(request):
    params = {}
    post_list = Post.objects.all()
    params['post_list'] = post_list
    return render(request, 'alVatross/post.html', params)

@login_required
def insert(request):
    params = {
        'add_post_form': AddPostForm(),
        'user': request.user
    }
    if request.method == 'POST':
        params["add_post_form"] = AddPostForm(data=request.POST)
        redirect_url = request.POST.get("redirect_url")
        post = Post(
            title   = request.POST.get("title"),
            content = request.POST.get("content"),
            status  = "active",
            user_id = request.POST.get("user_id"),
        )
        post.clean()
        if len(post.error_messages) == 0:
            post.save()
            return redirect(redirect_url)

        params['error'] = post.error_messages
        print(post.error_messages)
    return render(request, 'alVatross/insert_post.html', params)

@login_required
def update(request, id):
    post = Post.objects.get(id=id)
    params = {
        'edit_post_form': EditPostForm(instance=post),
        'user': request.user,
        'post': post
    }
    if request.method == 'POST':
        params["edit_post_form"] = EditPostForm(data=request.POST)
        redirect_url = request.POST.get("redirect_url")
        post = Post.objects.get(id=id)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.user_id = request.POST.get("user_id")
        post.clean()
        if len(post.error_messages) == 0:
            post.save()
            return redirect(redirect_url)

        params['error'] = post.error_messages
    return render(request, 'alVatross/update_post.html', params)

@login_required
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/alVatross/post')
