import imp
from django.urls import path
from . import views

urlpatterns = [
    path('test_celery/', views.test_celery, name='test_celery'),
    path('create_users/<str:num>/', views.create_users, name='create_users')
]
