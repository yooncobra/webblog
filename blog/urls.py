from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^posts/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^posts/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),

    url(r'^api/v1/', include('blog.api.v1', namespace='api_v1')),
    url(r'^api/v2/', include('blog.api.v2', namespace='api_v2')),
]