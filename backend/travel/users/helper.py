"""Module for helper functions"""
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def get_upload_path(instance, filename):
    """
    Creates image upload path dynamicly, depending on the uploading model.
    """
    model = instance.__class__
    name = model._meta.verbose_name_plural.replace(' ', '_')
    filename = str(instance)
    return f'static/{name}/images/{filename}'


def get_and_authenticate_user(email, password):
    """Authenticate user in during login and return instance of it."""
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError(
            "Invalid username/password. Please try again!")
    return user
