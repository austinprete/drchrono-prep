from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drchrono_prep.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
    url(r'^forms/', include('forms.urls', namespace='forms')),
    url(r'^', include('main.urls', namespace='main')),
)