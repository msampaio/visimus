from django.conf.urls.defaults import *

urlpatterns = patterns('visimus.contourweb.views',
    (r'^$', "contour_form"),
    (r'^show/$', "contour_show"),
    (r'^show_all/$', "contour_show_all"),
    (r'^show_one/$', "contour_show_one"),
)
