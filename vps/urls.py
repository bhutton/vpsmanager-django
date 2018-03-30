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
from vps import views

urlpatterns = [
	url(r'^(\d+)/$', views.view_vps, name='viewvps'),
    url(r'^create/', views.create_vps, name='createvps'),
    url(r'^modify/([0-9]+)', views.modify_vps, name='modifyvps'),
    url(r'^delete/([0-9]+)', views.delete_vps, name='deletevps'),
    url(r'^start/([0-9]+)', views.start_vps, name='startvps'),
    url(r'^stop/([0-9]+)', views.stop_vps, name='stopvps'),
    url(r'^snapshot/([0-9]+)', views.snapshot_vps, name='snapshot'),
    url(r'^status/([0-9]+)', views.status_vps, name='status')
]
