from django.contrib import admin
from django.urls import path, include

from accountapp.views import hello_world, AccountCreativeView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreativeView.as_view(), name='create'), # 클래스형뷰는 as_view()를
]
