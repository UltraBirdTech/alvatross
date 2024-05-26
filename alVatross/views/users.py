from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.models import User
from ..form.user import UserForm
from ..form.user_update import UserUpdateForm
from ..models.logger import Logger
from ..form.user_type_form import UserTypeChoiceForm

logger = Logger()
@login_required
def index(request):
    logger.log_info('Access to User List.')
    query= request.GET.get("query", "")
    user_type = request.GET.get("user_type")
    params = {
        'login_user': request.user,
        'user_type_choice_form': UserTypeChoiceForm(selected_option=user_type)
    }
 
    user_list = User.objects.all()
    if query:
        user_list = User.objects.filter(
            Q(id__contains=query)|
            Q(first_name__contains=query)|
            Q(last_name__contains=query)|
            Q(email__contains=query)
        )

    if user_type == 'Admin' or user_type == 'User':
        user_list = User.objects.filter(is_superuser=user_type=='Admin')

    params['user_list'] = user_list
    params['query'] = query
    return render(request, 'alvatross/user.html', params)

@login_required
def insert(request):
    logger.log_info('Access to Insert User.')
    params = {
        'add_user_form': UserForm(),
        'login_user': request.user
    }
    if request.method == 'POST':
        params["add_user_form"] = UserForm(data=request.POST)

        user = User(
            username = request.POST.get("username"),
            email = request.POST.get("email"),
            password = request.POST.get("password")[0:20],
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            is_superuser = request.POST.get("is_superuser")
        )

        # duplicate check.
        if User.objects.filter(username=user.username):
             error_message = '指定されたusernameは既に登録されています'
             params['error'] = [error_message]
             logger.log_warn(error_message)
             return render(request, 'alvatross/insert_user.html', params)

        if not user.clean():
            user.save()
            logger.log_info('Insert User is success.')
            return redirect('/alVatross/users/?success_message=ユーザの新規登録に成功しました。')

        params['error'] = user.error_messages
        logger.log_warn(user.error_messages[0])
    return render(request, 'alvatross/insert_user.html', params)

@login_required
def update(request, id):
    logger.log_info('Access to Update User.')
    user = User.objects.get(id=id)
    params = {
        'edit_user_form': UserUpdateForm(instance=user),
        'login_user': request.user,
        'user': user 
    }
    if request.method == 'POST':
        params["edit_post_form"] = UserForm(data=request.POST)
        user = User.objects.get(id=id)
        user.email = request.POST.get("email")
        user.password = request.POST.get("new_password")[:20]
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")

        if not user.clean():
            user.save()
            logger.log_info('Update User is sucsess.')
            logger.log_info('Update User Id: [' + str(user.id) + ']')
            return redirect('/alVatross/users/?success_message=ユーザの更新に成功しました。')

        params['error'] = post.error_messages
    return render(request, 'alvatross/update_user.html', params)

@login_required
def delete(request, id):
    user= User.objects.get(id=id)
    params = {}
    if request.user.id == id:
        error_message = '自分自身を削除することはできません'
        params['error'] = [error_message]
        logger.log_warn(error_message)
        return render(request, 'alvatross/user.html', params)

    if user.is_superuser:
        error_message = '管理者権限ユーザは削除できません'
        params['error'] = [error_message]
        logger.log_warn(error_message)
        return render(request, 'alvatross/user.html', params)
        
    user.delete()
    logger.log_info('Delete User is sucsess.')
    logger.log_info('Delete User Id: [' + str(user.id) + ']')
    return redirect('/alVatross/users/?success_message=ユーザの削除に成功しました。')
