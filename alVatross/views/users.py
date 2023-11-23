from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from ..form.user import UserForm

@login_required
def index(request):
    params = {
        'login_user': request.user
    }
    user_list = User.objects.all()
    params['user_list'] = user_list
    return render(request, 'alVatross/user.html', params)

@login_required
def insert(request):
    params = {
        'add_user_form': UserForm(),
        'login_user': request.user
    }
    if request.method == 'POST':
        params["add_user_form"] = UserForm(data=request.POST)
        redirect_url = request.POST.get("redirect_url")
        user = User(
            username = request.POST.get("username"),
            email = request.POST.get("email"),
            password = request.POST.get("password")
        )
        user.save()
        return redirect('/alVatross/users/')

        params['error'] = post.error_messages
        print(user.error_messages)
    return render(request, 'alVatross/insert_user.html', params)

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