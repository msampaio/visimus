from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('visimus.matrix.views',
    (r'^$', "main_page"),
    (r'^matrix/$', "matrix_form"),
    (r'^matrix/show/$', "matrix_show"),

)

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
