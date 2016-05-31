import os
import sys
from django.conf.urls import url
from django.http import HttpResponse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)

'''How to run

python micro_django.py runserver
'''

DEBUG = True
SECRET_KEY = 'foo'

urlpatterns = [
    url(r'^$', lambda request: HttpResponse('hello world')),
    url(r'^(?P<name>\w+)/$', lambda request, name: HttpResponse('hello, {}'.format(name))),
]

ROOT_URLCONF = __name__

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)