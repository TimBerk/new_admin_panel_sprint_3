from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

from django.urls import include, path

from config import __version__


schema_view = get_schema_view(
    openapi.Info(
        title='Онлайн-кинотеатр',
        default_version=__version__,
        description='Сервис для работы с фильмами',
        license=openapi.License(name='BSD License'),
    ),
    patterns=[path('', include('config.urls'))],
    authentication_classes=(BasicAuthentication,),
    permission_classes=(permissions.AllowAny,),
    public=True
)
