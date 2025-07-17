# D:\GitDjangoDemo\AlgoDemo\AlgoDemoApp\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('regex/', views.regex_topics, name='regex_topics')
]
