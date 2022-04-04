from django.urls import path, re_path

from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView

urlpatterns = [
    # WEB Urls
    path('login/', LoginView.as_view(), name='users_login'),
    path('logout/', LogoutView.as_view(), name='users_logout'),

    # API Urls
    path('api/1.0/users/', UserListAPI.as_view(), name='api_user_list'),
    re_path(r'api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail'),
]