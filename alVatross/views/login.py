from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout # logout() だと 本ソースコードの logout()と競合するため名前を変えている。
from django.db.models import Q
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import User

from django.template import Engine
from django.template import Context, Template
from django.template import RequestContext
from django.http import HttpResponse

from ..models.logger import Logger

def index(request):
    logger = Logger()
    params = {}
    if request.method == 'POST':
        logger.log_info('Start Login process.')
        name = request.POST.get('loginid', None)
        password = request.POST.get('password', None)
        user_list = User.objects.filter(username=name)
        if len(user_list) == 0:
            error_message = "指定されたユーザが存在しません。" + "[" + name + "]"
            logger.log_warn(error_message)
            params['error'] = [error_message]
            return render(request, 'alvatross/login.html', params)

        # user は loginid で検索した場合は一意なのでゼロ要素目を取得する。
        user = user_list[0]
        if check_password(password, user.password):
            login(request, user)
            logger.log_info('Login is Success.' + '[' + user.name + ']')
            return redirect('/alVatross/')

        # [MEMO]: 脆弱性。ハッシュされていないパスワードでもチェックしてログインさせる。
        if password == user.password:
            login(request, user)
            logger.log_info('Login is Success as not hash.')
            return redirect('/alVatross/')

        error_message = "パスワードが間違っています。"
        logger.log_warn(error_message)
        params['error'] = [error_message]
        return render(request, 'alvatross/login.html', params)
    
    # Get Rquest.
    logger.log_info('Access to Login Page.')
    return render(request, 'alvatross/login.html', params)

def logout(request):
    logger = Logger()
    params = {}
    django_logout(request)
    logger.log_info('Logout is Success.')
    return redirect('/alVatross/login')

def forget_password(request):
    params = {}
    logger = Logger()

    if request.method == 'POST':
        logger.log_info('Start Pasword Remind.')
        name = request.POST.get('loginid', None)
        user_list = User.objects.filter(username=name)
        if len(user_list) == 0:
            error_message = "指定されたユーザが存在しません。"
            logger.log_warn(error_message)
            params['error'] = [error_message]
            return render(request, 'alvatross/forget_password.html', params)
        
        user = user_list[0]
        template_code = '<!DOCTYPE html><html><body>\
            There are Your ID and Password.<br>\
            Login ID: ' + str(user.id) +'<br>\
            Name: ' + user.first_name + user.last_name +'<br>\
            Password: '+user.password+'<br>\
            </body></html>\
        '
        engine = Engine()
        template = engine.from_string(template_code=template_code)
        context = RequestContext(request)
        context.push({"name": "TEST"})
        logger.log_info('Password Remind is success.')
        return HttpResponse(template.render(context), request)

    logger.log_info('Access to Password Remind.')
    return render(request, 'alvatross/forget_password.html', params)
