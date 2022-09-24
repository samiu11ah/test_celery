from django.shortcuts import render
from django.http import HttpResponse
from .tasks import testwhile, create_users_in_bg
from django.contrib.auth.models import User
 

def create_users(request, num):
    create_users_in_bg.delay(int(num))
    return HttpResponse(f'{num} random users are being created in background')


def test_celery(request):
    context = {}
    for user in User.objects.all().exclude(is_superuser=True):
        testwhile.delay(user.username)

    
    return render(request, 'base/test_celery.html', context)