import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    """User in the system"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    verification_status = models.CharField(max_length=255)
    address_history_status = models.CharField(max_length=255)
    kyc_status = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class UserToken(models.Model):
    user_id = models.UUIDField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

class Reset(models.Model):
    email = models.EmailField(max_length=255)
    token = models.CharField(max_length=255, unique=True)

