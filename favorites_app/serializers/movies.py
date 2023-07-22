from rest_framework import serializers
from favorites_app.models.movies import Movie
from favorites_app.models.favorites import Favorite

class MovieSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'url', 'created', 'updated', 'is_favorite']

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.query_params.get('user_id'):
            user_id = int(request.query_params.get('user_id'))
            return Favorite.objects.filter(user_id=user_id, movie=obj).exists()
        return False

    def get_title(self, obj):
        request = self.context.get('request')
        if request and request.query_params.get('user_id'):
            user_id = int(request.query_params.get('user_id'))
            if Favorite.objects.filter(user_id=user_id, movie=obj).exists():
                favorite = Favorite.objects.get(user_id=user_id, movie=obj)
                return favorite.custom_name
        return obj.title

