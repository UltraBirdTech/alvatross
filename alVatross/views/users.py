from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.models import User
from ..form.user import UserForm

@login_required
def index(request):
    params = {
        'login_user': request.user
    }
    user_list = User.objects.all()
    query= request.GET.get("query", None)
    user_type = request.GET.get("user_type")
    user_list = User.objects.all()
    if query:
        user_list = User.objects.filter(
            Q(id__contains=query)|
            Q(first_name__contains=query)|
            Q(last_name__contains=query)|
            Q(email__contains=query)
        )

    is_staff = ''
    if user_type == 'Admin':
        is_staff = True
    elif user_type == "User":
        is_staff = False
        
    if user_type != 'All':
        user_list = User.objects.filter(is_staff=is_staff)

    params['user_list'] = user_list
    params['query'] = query
    return render(request, 'alvatross/user.html', params)

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
            password = request.POST.get("password")[0:20],
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name")
        )

        # duplicate check.
        if User.objects.filter(username=user.username):
             params['error'] = ['指定されたusernameは既に登録されています']
             return render(request, 'alvatross/insert_user.html', params)

        if not user.clean():
            user.save()
            return redirect('/alVatross/users/')

        params['error'] = user.error_messages
    return render(request, 'alvatross/insert_user.html', params)

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
        user.password = request.POST.get("password")[:20]
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")

        # duplicate check.
        if User.objects.filter(username=user.username):
            params['error'] = ['指定されたusernameは既に登録されています']
            return render(request, 'alvatross/update_user.html', params)

        if not user.clean():
            user.save()
            return redirect('/alVatross/users/')

        params['error'] = post.error_messages
    return render(request, 'alvatross/update_user.html', params)

@login_required
def delete(request, id):
    user= User.objects.get(id=id)
    params = {}
    if request.user.id == id:
        params['error'] = '自分自身を削除することはできません'
        return render(request, 'alvatross/user.html', params)

    if user.is_superuser:
        params['error'] = '管理者権限ユーザは削除できません'
        return render(request, 'alvatross/user.html', params)
        
    user.delete()
    return redirect('/alVatross/users')
