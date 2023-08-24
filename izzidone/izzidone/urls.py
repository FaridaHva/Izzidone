from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),  
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('users/', include('users.urls')),
    path(
        "",
        views.PasswordReset.as_view(),
        name="request-password-reset",
    ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        views.ResetPasswordAPI.as_view(),
        name="reset-password",
    ),
    path('services/', include('services.urls')),
]

