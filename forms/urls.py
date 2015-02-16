from django.conf.urls import patterns, url
from forms import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^newuser/$', views.new_user, name='new_user'),
                       url(r'^newuser/create/$', views.create_user, name='create_user'),
                       url(r'^login/$', views.login_view, name='login'),
                       url(r'^logout/$', views.logout_view, name='logout'),
                       url(r'^(?P<user_id>\d+)/$', views.user, name='user'),
                       url(r'^(?P<user_id>\d+)/newform/$', views.new_form, name='new_form'),
                       url(r'^(?P<user_id>\d+)/newform/create/$', views.create_form, name='create_form'),
                       url(r'^(?P<user_id>\d+)/(?P<form_id>\d+)/$', views.form, name='form'),
                       url(r'^(?P<user_id>\d+)/(?P<form_id>\d+)/addelement/$', views.add_element, name='add_element'),
                       url(r'^(?P<user_id>\d+)/(?P<form_id>\d+)/share', views.share_form, name='share_form'),
                       url(r'^form/(?P<form_id>\d+)/$', views.view_form, name='view_form'),
)