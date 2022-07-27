from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('news_list/', news, name='news'),
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>', new1, name='new1'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('', IndexView.as_view()),
    path('login/', LoginView.as_view(template_name = 'news/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'news/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name = 'news/signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('accounts/', include('allauth.urls')),
]