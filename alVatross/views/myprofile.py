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

    #template_engine = Engine()
   # layout_template = loader.get_template('layout.html')
    index_template = loader.get_template('myprofile.html')
    index_html = index_template.render(params)
    print(index_html)
    index_html = index_html.replace('#LAST_NAME#', request.user.last_name)
    index_html = index_html.replace('#FIRST_NAME#', request.user.first_name)
    print(index_html)
   # result_html = layout_template.render({'content': index_html})
    #return HttpResponse(result_html)
    
    
    return HttpResponse(index_html)


    template_html = '<!DOCTYPE html><html><body>\
    <div class="test">\
    {% block layout %}{layout_template.render(params)}{% endblock %}\
    {layout_template}\
    </div>\
    {% block title %} alVatross {% endblock %}\
    {% block content %}\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello '+request.user.username+'</h2>\
    {% endblock %}\
    </body></html>'
    base_template = template_engine.from_string(template_code=template_html)


    base_template = loader.get_template('index.html')
    params = {
        'login_user': request.user,
        'layout': layout_template
    }

    context = Context(params)
#    result_html = base_template.render({'layout': layout_template.render(context)})
    result_html = base_template.render(context)
   
    return HttpResponse(result_html)
