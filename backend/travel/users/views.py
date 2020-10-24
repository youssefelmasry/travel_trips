"""Custom User Views."""
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS

from .serializers import CustomUserSerializer, SignUpSerializerWithToken


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    Provides .list(), .retrieve(), .create(), .update(),
    .partial_update(),and .destroy() actions for CustomUser model.
    """
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CustomUserSerializer
        else:
            return SignUpSerializerWithToken

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
