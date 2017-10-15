"""vpsmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from vps import views
from vps import urls as vps_urls


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    # url(r'^vps/', include('vps.urls')),
    url(r'^vps/', include(vps_urls)),
    # url(r'^createvps/', views.create_vps, name='createvps'),
    # url(r'^createuser/', views.create_user, name='createuser'),
    # url(r'^lists/', include(vps_urls)),
    # url(r'^admin/', admin.site.urls),
]