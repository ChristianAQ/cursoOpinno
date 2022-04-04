from django.urls import path, re_path

from photos.api import PhotoListAPI, PhotoDetailAPI
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView


class PhotoDetailAPIView:
    pass


urlpatterns = [
    path('create/', PhotoCreationView.as_view(), name='photos_create'),
    path('photos/', PhotoListView.as_view(), name='photos_my_photos'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    path('', HomeView.as_view(), name='photos_home'),
    re_path(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='api_photos_list'),
    re_path(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='api_photos_detail'),
]