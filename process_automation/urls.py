
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Automation API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    re_path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path('admin/', admin.site.urls),
    re_path('accounts/', include('accounts.urls')),
    re_path('catalog/', include('catalog.urls')),
    re_path('general/', include('general.urls')),
    re_path('orders/', include('orders.urls')),
    re_path('security/', include('security.urls')),
    re_path('auth/', include('dj_rest_auth.urls')),
    re_path('auth/registration/', include('dj_rest_auth.registration.urls'))

]
