from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="AI Bot API",
        default_version='v1',
        description="API for interacting with AI Bot",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourcompany.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Admin conf
admin.site.site_header = "UniWay Adminstration"
admin.site.index_title = "Homepage"
admin.site.site_header = "UniWay Adminstration"

api_urls = [
    path("users/", include("users.urls")),
    path("about/", include("about.urls")),
    path("university/", include("university.urls")),
    path("exam/", include("exam.urls")),
    path("aibot/", include("aibot.urls")),
    path("payment/", include("payment.urls")),
    path("recomendation/", include("recomendation.urls")),

    # Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(api_urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
