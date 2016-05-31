from django.conf.urls import url
from django.contrib.auth.views import login
from accounts.forms import LoginForm
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login/$', login, kwargs={
        'authentication_form': LoginForm,
    }),
    url(r'^profile/$', views.profile),
]