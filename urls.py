from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^tabnu/', include('tabnu.app.urls')),
)
