"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.list_user, name='users'),
    url(r'^(\d+)/$', views.view_user, name='view_user'),
    url(r'^create/', views.create_user, name='createuser'),
    url(r'^modify/([0-9]+)', views.modify_user, name='modifyuser'),
    url(r'^delete/([0-9]+)', views.delete_user, name='modifyuser'),
]
