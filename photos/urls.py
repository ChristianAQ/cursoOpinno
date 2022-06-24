from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView, GalleryFemale, About, Contact

router = DefaultRouter()
router.register('api/1.0/photos', PhotoViewSet, basename='api_photos_')

urlpatterns = [
    path('create/', PhotoCreationView.as_view(), name='photos_create'),
    path('photos/', PhotoListView.as_view(), name='photos_my_photos'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    path('', HomeView.as_view(), name='photos_home'),
    path('GalleryFemale/', GalleryFemale, name="gallery_female"),
    path('About/', About, name="about"),
    path('Contact/', Contact, name="contact"),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)