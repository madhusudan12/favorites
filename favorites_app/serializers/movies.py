from rest_framework import serializers
from favorites_app.models.movies import Movie

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model.
    """
    class Meta:
        model = Movie
        fields = '__all__'

