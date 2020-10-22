"""Custom User serilazers."""
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize CustomUser Information into JSON."""
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']
