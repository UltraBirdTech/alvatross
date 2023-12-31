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
        user.clean()
        user.save()
        return redirect('/alVatross/users/')

        params['error'] = user.error_messages
        print(user.error_messages)
    return render(request, 'alVatross/insert_user.html', params)

@login_required
def update(request, id):
    user = User.objects.get(id=id)
    params = {
        'edit_user_form': UserForm(instance=user),
        'login_user': request.user,
        'user': user 
    }
    if request.method == 'POST':
        params["edit_post_form"] = UserForm(data=request.POST)
        user = User.objects.get(id=id)
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        if not user.clean():
            user.save()
            return redirect('/alVatross/users/')

        params['error'] = post.error_messages
    return render(request, 'alVatross/update_user.html', params)

@login_required
def delete(request, id):
    user= User.objects.get(id=id)
    params = {}
    if user.id == id:
        params['error'] = '自分自身を削除することはできません'

    if user.is_superuser:
        params['error'] = '管理者権限ユーザは削除できません'
        
    user.delete()
    return redirect('/alVatross/users')
