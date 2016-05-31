from django.conf.urls import url
from django.http import JsonResponse


def post_list(request):
    return JsonResponse({'posts': []}, safe=False)


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
]