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

def index(request):
    params = {}
    if request.method == 'POST':
        name = request.POST.get('loginid', None)
        password = request.POST.get('password', None)
        user_list = User.objects.filter(username=name)
        if len(user_list) == 0:
            error_message = "指定されたユーザが存在しません。"
            params['error'] = [error_message]
            return render(request, 'alVatross/login.html', params)

        # user は loginid で検索した場合は一意なのでゼロ要素目を取得する。
        user = user_list[0]
        if check_password(password, user.password):
            login(request, user)
            return redirect('/alVatross/')

        # [MEMO]: 脆弱性。ハッシュされていないパスワードでもチェックしてログインさせる。
        if password == user.password:
            login(request, user)
            return redirect('/alVatross/')

        error_message = "パスワードが間違っています。"
        params['error'] = [error_message]
        return render(request, 'alVatross/login.html', params)
    
    # Get Rquest.
    return render(request, 'alVatross/login.html', params)

def logout(request):
    params = {}
    django_logout(request)
    return redirect('/alVatross/login')

def forget_password(request):
    params = {}

    if request.method == 'POST':
        name = request.POST.get('loginid', None)
        user_list = User.objects.filter(username=name)
        if len(user_list) == 0:
            error_message = "指定されたユーザが存在しません。"
            params['error'] = [error_message]
            return render(request, 'alVatross/forget_password.html', params)
        
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
        return HttpResponse(template.render(), request)

    return render(request, 'alVatross/forget_password.html', params)
