from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth.models import User
from faker import Faker
from .models import Model_detail
fake = Faker()


@shared_task
def testwhile(username):
    user = User.objects.get(username=username)
    while Model_detail.objects.get(user=user).is_running:
        print(str(user)+ 'is running')




@shared_task
def create_users_in_bg(num):
    for i in range(num):
        user = User.objects.create_user(username=fake.simple_profile()['username'], email=fake.email(), password="Kingsmen786")
        model_details = Model_detail(user=user)
        model_details.save()
        print(f'{i} user with model details created created')