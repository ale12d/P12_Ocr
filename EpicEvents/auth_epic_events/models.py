from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SUPPORT = 1
    SELLER = 2

    ROLE_CHOICES = (
        (SUPPORT, 'Support'),
        (SELLER, 'Seller'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,
                                            blank=True, null=True)
