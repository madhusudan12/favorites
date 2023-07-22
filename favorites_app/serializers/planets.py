from rest_framework import serializers
from favorites_app.models.planets import Planet


class PlanetSerializer(serializers.ModelSerializer):
    """
    Serializer for Planet model.
    """
    class Meta:
        model = Planet
        fields = '__all__'
