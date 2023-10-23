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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alVatross/login', views.login.index, name='login'),
    path('alVatross/logout', views.login.logout, name='logout'),
    path('alVatross/post/', views.post.index, name='post'),
    path('alVatross/post/insert', views.post.insert, name='insert_post'),
    path("alVatross/post/<int:id>", views.post.update, name='update_post'),
    path('alVatross', views.index.index, name='index'),
]
