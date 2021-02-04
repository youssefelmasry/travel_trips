"""Custom User Models."""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

def get_upload_path(instance, filename):
    """
    Creates image upload path dynamically, depending on the uploading model.
    """
    model = instance.__class__
    name = model._meta.verbose_name_plural.replace(' ', '')
    filename = f"{instance.email.split('@')[0]}.{filename.split('.')[-1]}"
    return f'{name}/images/{filename}'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with email as the unique identifier.
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to=get_upload_path, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(_("is active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta Info."""

        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """Use email as string representation."""
        return self.email
