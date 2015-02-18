from django.conf.urls import patterns, url
from schedule import views

urlpatterns = patterns('',
                       url(r'^(?P<family_id>\d+)/(?P<member_id>\d+)/chart/$', views.chart, name='chart'),
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<family_id>\d+)/(?P<member_id>\d+)/chart/update', views.update_schedule, name="update"),
                       url(r'^newfamily/$', views.new_family_view, name='new_family'),
                       url(r'^newfamily/add/', views.add_family, name='add_family'),
                       url(r'^(?P<family_id>\d+)/$', views.family_view, name='family'),
                       url(r'^(?P<family_id>\d+)/add', views.add_member, name='add_member')

)