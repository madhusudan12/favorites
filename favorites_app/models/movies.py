import uuid
from django.db import models


class Movie(models.Model):
    """
    Represents a Star Wars movie.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    url = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

