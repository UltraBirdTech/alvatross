from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.template import Engine
from django.template import RequestContext
from django.http import HttpResponse

@login_required
def index(request, id):
    user = User.objects.get(id=id)
    params = {
        'login_user': request.user
    }

    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello '+user.username+'</h2></body></html>'

    engine = Engine()
    template = engine.from_string(template_code=template)
    context = RequestContext(request)
    #context.push({"name": user.first_name})
    return HttpResponse(template.render(context))
