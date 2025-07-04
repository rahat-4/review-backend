import uuid

from django.db import models


class BaseModel(models.Model):
    """
    An abstract base model that provides common fields and methods for all models.
    """

    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Unique Identifier",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"
