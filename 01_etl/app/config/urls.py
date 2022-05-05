from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from config.helpers.yasg import schema_view
from movies.api import urls as movies_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema-ui'),
    re_path(r'api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(movies_urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
