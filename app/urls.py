from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'tabnu.app.views.index'),
	(r'^(?P<tab_name>[A-Z,a-z,0-9,\-,\_]+)/$', 'tabnu.app.views.tab'),
)

