from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    params = {}
    return render(request, 'alVatross/index.html', params)
