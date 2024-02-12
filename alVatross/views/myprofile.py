from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.template import Context, Engine, loader
from django.template import RequestContext
from django.http import HttpResponse

@login_required
def index(request):
    params = {
        'login_user': request.user,
    }
    print(request.user)

    return render(request, 'alvatross/myprofile.html', params)
