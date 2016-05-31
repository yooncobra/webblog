from django.conf.urls import url
from django.contrib.auth.views import login
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^login/$', login, kwargs={
        'authentication_form': LoginForm,
    }),
]