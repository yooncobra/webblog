from django.conf.urls import url
from django.contrib.auth.views import login
from accounts.forms import LoginForm
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^signup/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.signup_confirm),
    url(r'^login/$', login, kwargs={
        'authentication_form': LoginForm,
    }),
    url(r'^profile/$', views.profile),
]