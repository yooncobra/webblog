from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login),
]