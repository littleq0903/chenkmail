from django.conf.urls.defaults import *
from django.conf import *


urlpatterns = patterns('mail',
        url(r'^$', 'views.index'),
        )
