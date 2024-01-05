from enum import unique
from django.db import models
import uuid
from django_extensions.db.models import AutoSlugField


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="devices",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.id}"
