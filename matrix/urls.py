from django.conf.urls.defaults import *


urlpatterns = patterns('visimus.matrix.views',
    (r'^$', "matrix_form"),
    (r'^show/$', "matrix_show"),
)
