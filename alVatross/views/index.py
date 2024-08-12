from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.logger import Logger

logger = Logger()
@login_required
def index(request):
    logger.log_info("accsess to index page.")
    params = {}
    return render(request, 'alvatross/index.html', params)
