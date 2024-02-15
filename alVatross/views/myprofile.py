from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    params = {
        'login_user': request.user,
    }

    return render(request, 'alvatross/myprofile.html', params)
