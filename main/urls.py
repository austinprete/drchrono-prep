from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login', views.login_view, name='login'),
                       url(r'^logout', views.logout_view, name='logout'),
                       url(r'^user/', views.user, name='user'),
                       )