from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
import csv
import urllib

from ..models.post import Post
from django.contrib.auth.models import User
from ..models.logger import Logger
from ..form.post import AddPostForm, EditPostForm

@login_required
def index(request):
    logger = Logger()
    logger.log_info('Access to Post List.')
    params = {}
    query= request.GET.get("query", None)
    params['user_list'] = User.objects.all()

    if query:
        post_list = Post.objects.raw('SELECT * FROM alvatross_post WHERE title=%s or content=%s', [query, query])
    else:
        post_list = Post.objects.all()

    params['post_list'] = post_list
    return render(request, 'alvatross/post.html', params)

def csv_export(request):
    logger = Logger()
    logger.log_info('Access to Export post as csv.')
    params = {}
    # create response.
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    date_time = datetime.datetime.now()
    str_time = date_time.strftime('%Y%m%d%H%M')
    f = "Post" + "_" + str_time + ".csv" 
    file_name = urllib.parse.quote((f).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(file_name)

    # search post.
    query= request.GET.get("query", None)
    if query:
        post_list = Post.objects.raw('SELECT * FROM alvatross_post WHERE title=%s or content=%s', [query, query])
    else:
        post_list = Post.objects.all()

    writer = csv.writer(response)
    writer.writerow(['ID', 'TITLE', 'CONTENT', 'USER', 'CREATED AT', 'UPDATED AT'])
    for post in post_list:
        writer.writerow([post.id, post.title, post.content, post.user, post.created_at, post.updated_at])

    return response

@login_required
def insert(request):
    logger = Logger()
    logger.log_info('Access to Insert Post.')
    params = {
        'add_post_form': AddPostForm(),
        'user': request.user
    }
    if request.method == 'POST':
        params["add_post_form"] = AddPostForm(data=request.POST)
        post = Post(
            title   = request.POST.get("title"),
            content = request.POST.get("content"),
            status  = "active",
            user_id = request.POST.get("user_id"),
        )
        post.clean()
        if len(post.error_messages) == 0:
            post.save()
            logger.log_info('Insert Post is success.')
            redirect_url = request.POST.get("redirect_url")
            redirect_url = redirect_url + '?success_message=POSTの投稿に成功しました。'
            return redirect(redirect_url)

        params['error'] = post.error_messages
        logger.log_info(post.error_messages[0])
    return render(request, 'alvatross/insert_post.html', params)

@login_required
def update(request, id):
    logger = Logger()
    logger.log_info('Access to Update Post.')
    post = Post.objects.get(id=id)
    params = {
        'edit_post_form': EditPostForm(instance=post),
        'user': request.user,
        'post': post
    }
    if request.method == 'POST':
        params["edit_post_form"] = EditPostForm(data=request.POST)
        post = Post.objects.get(id=id)
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.clean()
        if len(post.error_messages) == 0:
            post.save()
            logger.log_info('Update Post is success.')
            logger.log_info('Update Post Id: [' + str(post.id) + ']')
            redirect_url = request.POST.get("redirect_url")
            redirect_url = redirect_url + '?success_message=POSTの更新に成功しました。'
            return redirect(redirect_url)

        params['error'] = post.error_messages
        logger.log_info(post.error_messages[0])
    return render(request, 'alvatross/update_post.html', params)

@login_required
def delete(request, id):
    logger = Logger()
    logger.log_info('Access to Delete Post.')
    post = Post.objects.get(id=id)
    post.delete()
    logger.log_info('Delete Post is sucess.')
    logger.log_info('Delete Post Id: [' + str(post.id) + ']')
    return redirect('/alVatross/post?success_message=POSTの削除に成功しました。')
