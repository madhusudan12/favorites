import uuid
from django.db import models
from favorites_app.models.movies import Movie
from favorites_app.models.planets import Planet


class FavoriteChoices(models.TextChoices):
    MOVIE = "movie"
    PLANET = "planet"


class Favorite(models.Model):
    """
    Represents a user's favorite Star Wars movie or planet.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    content_type = models.CharField(max_length=10, choices=FavoriteChoices.choices)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE, related_name='favorites')
    planet = models.ForeignKey(Planet, null=True, blank=True, on_delete=models.CASCADE, related_name='favorites')
    custom_name = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     # Ensure the combination of user_id, content_type, and object_id is unique
    #     unique_together = ['user_id', 'movie', 'planet']

    def __str__(self):
        return f"Favorite: {self.custom_name or self.movie or self.planet}"

