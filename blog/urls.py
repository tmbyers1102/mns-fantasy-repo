from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from rest_framework import format_suffix_patterns
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PlayersListView,
    PlayersDetailView,
    UserPlayerListView,
    PlayersCreateView,
    PlayersUpdateView,
    PlayersDropView,
    get_data,
    ChartData,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('players/new/', PlayersCreateView.as_view(), name='players-create'),
    path('players/<int:pk>/update/', PlayersUpdateView.as_view(), name='players-update'),
    path('players/<int:pk>/drop/', PlayersDropView.as_view(), name='players-drop'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('players/', PlayersListView.as_view(), name='blog-players'),
    path('players/<int:pk>/', PlayersDetailView.as_view(), name='players-detail'),
    path('user_players/<str:username>/', UserPlayerListView.as_view(), name='user-players'),
    path('players/<id>/updating/', views.player_update, name="player-updating"),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^stats', views.playerStatList.as_view()),
]

''' When you go to add the listview of something so it appears on the front end,
the convention it will look for (aka the file folder path it requires is:
<app>/<model>_<viewtype>.html

For the blog posts its looking for app: blog, model: post, viewtype: list
'''

urlpatterns += staticfiles_urlpatterns()