from rest_framework.routers import DefaultRouter

from django.urls import include, path

from movies.api.v1.views import MovieViewSet


router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls))
]
