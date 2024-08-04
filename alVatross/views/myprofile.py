from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from ..models.logger import Logger

logger = Logger()
@login_required
def index(request):
    logger.log_info('Access to Myprofile')
    params = {
        'login_user': request.user,
    }

    return render(request, 'alvatross/myprofile.html', params)
