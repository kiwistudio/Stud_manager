from django.conf.urls import patterns, include, url
from django.contrib import admin

from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('student.urls'))
)



if DEBUG:
	# serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
		)