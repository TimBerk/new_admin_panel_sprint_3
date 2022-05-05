import uuid

from rest_framework import mixins, viewsets

from django.db import models
from django.utils.translation import gettext as _


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modified'), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ListRetrieveAPIView(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """Mixin for reading records."""
    pass
