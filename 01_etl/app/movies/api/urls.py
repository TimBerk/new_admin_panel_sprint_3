from django.urls import include, path

from movies.api.v1 import urls as movies_urls


urlpatterns = [
    path('v1/', include(movies_urls))
]
