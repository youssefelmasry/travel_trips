"""Custom User Manager."""
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager model where email is the unique identifier
    for authentication instead of username.
    """

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create and save user with given email and password."""
        fields_names = ["email", ]
        values = [email, ]
        field_value_map = dict(zip(fields_names, values))
        for field, value in field_value_map.items():
            if not value:
                raise ValueError(_(f"The {field} must be set!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creaete and save superuser with email,
        password and correct defaults.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
