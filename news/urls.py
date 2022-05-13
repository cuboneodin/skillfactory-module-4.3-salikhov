from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('news_list/', news, name='news'),
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>', new1, name='new1'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]