from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from cinematica.urls import cinematic_routes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('cinematica.urls')),
    path('api/v1/cinematica/', include(cinematic_routes.urls)),
]

if settings.DEBUG:

    schema_view = get_schema_view(
        openapi.Info(
            title='Online cinemantica API',
            default_version='v1',
            description='Online cinemantica API',
            terms_of_service='',
            contact=openapi.Contact(email='whoiam@gmail.com'),
        ),
        public=True,
        permission_classes=[permissions.AllowAny, ],
    )
    urlpatterns = urlpatterns + [
        path(r'api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]