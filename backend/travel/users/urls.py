"""Custom User URL configration."""
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from .views import CustomUserViewSet

router = SimpleRouter()

router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]+router.urls
