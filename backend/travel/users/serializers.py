"""Custom User serilazers."""
from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation

from .helper import get_tokens_for_user


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize CustomUser Information into JSON."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'first_name',
                  'last_name', 'photo']


class SignUpSerializerWithToken(serializers.ModelSerializer):
    """SignUp a user and get access token."""

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


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                'Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class SocialSerializer(serializers.Serializer):
    """Serializer which accepts an OAuth2 access token."""
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
