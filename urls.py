from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': "main_page.html"}),
    (r'^matrix/', include('matrix.urls')),
    (r'^contour/', include('contourweb.urls')),
    (r'^harmony/', include('harmony.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
