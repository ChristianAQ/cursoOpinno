from django.urls import path, re_path
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView


urlpatterns = [
    path('create/', PhotoCreationView.as_view(), name='photos_create'),
    path('photos/', PhotoListView.as_view(), name='photos_my_photos'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    path('', HomeView.as_view(), name='photos_home'),
]
