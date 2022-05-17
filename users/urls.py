from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView

router = DefaultRouter()
router.register('api/1.0/users', UserViewSet, basename='api_users_')

urlpatterns = [
    # WEB Urls
    path('login/', LoginView.as_view(), name='users_login'),
    path('logout/', LogoutView.as_view(), name='users_logout'),

    # API Urls
    path('', include(router.urls))
]
