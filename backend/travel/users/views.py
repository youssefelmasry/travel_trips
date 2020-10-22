"""Custom User Views."""
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    Provides .list(), .retrieve(), .create(), .update(),
    .partial_update(),and .destroy() actions for CustomUser model.
    """
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
