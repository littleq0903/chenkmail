from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chenkmail.views.home', name='home'),
    #url(r'^global/', include('chenkmail.apps.global.urls')),
    url(r'^mail/', include('chenkmail.apps.mail.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^manage/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
