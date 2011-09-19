from django.conf.urls.defaults import *

urlpatterns = patterns('visimus.contourweb.views',
    (r'^$', "contour_form"),
    (r'^show/$', "contour_show"),
)
