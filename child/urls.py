from django.conf.urls import patterns, url

from child import views

urlpatterns = patterns('',
  url(r'^$', views.child_list, name='child_list'),
  url(r'^add$', views.child_create, name='child_create'),
  url(r'^edit/(?P<pk>\d+)$', views.child_update, name='child_update'),
  url(r'^delete/(?P<pk>\d+)$', views.child_delete, name='child_delete'),
)