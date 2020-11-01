"""Custom User serilazers."""
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .helper import get_tokens_for_user


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize CustomUser Information into JSON."""
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']


class SignUpSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        return get_tokens_for_user(object)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['token', 'email', 'password', ]


class SocialSerializer(serializers.Serializer):
    """Serializer which accepts an OAuth2 access token."""
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
