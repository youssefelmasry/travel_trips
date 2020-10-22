"""Custom User URL configration."""
from django.urls import path, include
from rest_framework.routers import SimpleRouter


from .views import CustomUserViewSet

router = SimpleRouter()

router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = router.urls
