from django.conf.urls import patterns, include, url
from bookmarks.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('r^bookmarks/', include('bookmarks.urls')),
    url(r'^admin/', include(admin.site.urls)),
                       )