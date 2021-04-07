from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('rules/', views.rules, name='rules'),
    path('contact/', views.contact, name='contact'),
]