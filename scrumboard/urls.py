from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # scrumboard urls
    url(r'^', include('scrumboard.board.urls')),

    # auth
    # url(r'^auth/', include('auth.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
