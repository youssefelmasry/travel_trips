"""Custom User Models."""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from .helper import get_upload_path


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with email as the unique identifier.
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(
        _("first name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(
        _("last name"), max_length=50, blank=True, null=True)
    photo = models.FileField(_("photo"), upload_to=get_upload_path,
                             max_length=100, blank=True, null=True)
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
