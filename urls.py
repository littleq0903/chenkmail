from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', redirect_to, {'url': '/mail'}),
    url(r'^mail/', include('chenkmail.apps.mail.urls')),
    

    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^manage/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
