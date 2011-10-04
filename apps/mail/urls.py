from django.conf.urls.defaults import *
from django.conf import *


urlpatterns = patterns('mail.views',
        url(r'^$', 'index'),
        )
urlpatterns += patterns('mail.ajax',
        url(r'^ajax/sendmail$', 'sendmail'),
        )
urlpatterns += patterns('',
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout_then_login')
        )

