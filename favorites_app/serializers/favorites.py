from rest_framework import serializers
from favorites_app.models.favorites import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for Favorite model.
    """
    class Meta:
        model = Favorite
        fields = '__all__'
