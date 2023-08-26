from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


# provide name, username & kucoin details
class User(AbstractUser):
    """
    Custom User model
    all KuCoins details have been encrypted and stored in the database.
    """
    email = models.EmailField(_('email address'), unique=True)
