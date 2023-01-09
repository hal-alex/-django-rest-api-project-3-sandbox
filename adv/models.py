from django.db import models
import uuid

# Create your models here.

class Adv(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    owner = models.ForeignKey(
        'core.User',
        related_name="advs",
        on_delete = models.CASCADE
    )
