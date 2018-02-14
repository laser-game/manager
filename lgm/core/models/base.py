import uuid

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import (
    CreationDateTimeField,
    ModificationDateTimeField,
)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    x_created = CreationDateTimeField(_('created'))
    x_modified = ModificationDateTimeField(_('modified'))

    class Meta(object):
        abstract = True
