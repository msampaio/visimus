from django.conf.urls.defaults import *
from django.contrib.auth.views import login


urlpatterns = patterns('visimus.users.views',
    url(r'^login/$', login, name="login"),
    url(r'^dashboard/$', "dashboard", name="dashboard"),
    url(r'^logout/$', "logout", name="logout"),
    url(r'^deploy/$', "deploy", name="deploy"),
)
