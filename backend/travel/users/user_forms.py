"""Custom User forms."""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    """
    Form for Creating custom user.

    Creating user without profile, used in the admin site.
    """

    class Meta:
        """Meta Info."""

        model = get_user_model()
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """
    Form for Changing custom user data.

    Changing user without profile, used in the admin site.
    """

    class Meta:
        """Meta Info."""

        model = get_user_model()
        fields = ('email', 'password', 'is_active', 'is_staff',
                  'is_superuser')
