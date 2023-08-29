from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


# provide name, username & kucoin details
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    age = models.IntegerField(_('age'), default=1)


