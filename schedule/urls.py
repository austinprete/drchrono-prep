from django.conf.urls import patterns, url
from schedule import views

urlpatterns = patterns('',
                       url(r'^chart', views.chart, name='chart'),
                       url(r'^$', views.index, name='index'),
)