from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail),
    url(r'^posts/new/$', views.post_new),
    url(r'^posts/(?P<pk>\d+)/edit/$', views.post_edit),
    url(r'^posts/(?P<post_pk>\d+)/comments/new/$', views.comment_new),
    url(r'^posts/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit),
]