from rest_framework import serializers
from favorites_app.models.planets import Planet
from favorites_app.models.favorites import Favorite

class PlanetSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Planet
        fields = ['id', 'name', 'url', 'created', 'updated', 'is_favorite']

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.query_params.get('user_id'):
            user_id = int(request.query_params.get('user_id'))
            return Favorite.objects.filter(user_id=user_id, planet=obj).exists()
        return False

    def get_name(self, obj):
        request = self.context.get('request')
        if request and request.query_params.get('user_id'):
            user_id = int(request.query_params.get('user_id'))
            if Favorite.objects.filter(user_id=user_id, planet=obj).exists():
                favorite = Favorite.objects.get(user_id=user_id, planet=obj)
                return favorite.name
        return obj.name
