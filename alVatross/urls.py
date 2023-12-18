"""alVatross URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import login
from .views import index
from .views import post
from .views import users
from .views import myprofile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alVatross/', views.index.index, name='index'),
    path('alVatross/login', views.login.index, name='login'),
    path('alVatross/logout', views.login.logout, name='logout'),
    path('alVatross/post/', views.post.index, name='post'),
    path('alVatross/post/insert', views.post.insert, name='insert_post'),
    path("alVatross/post/<int:id>", views.post.update, name='update_post'),
    path("alVatross/post/delete/<int:id>", views.post.delete, name='delete_post'),
    path('alVatross/users/', views.users.index, name='user_list'),
    path('alVatross/users/insert', views.users.insert, name='insert_user'),
    path('alVatross/users/<int:id>', views.users.update, name='update_user'),
    path('alVatross/users/delete/<int:id>', views.users.delete, name='delete_user'),
    path("alVatross/myprofile", views.myprofile.index, name='myprofile'),
]
