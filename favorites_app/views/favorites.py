
from rest_framework import generics, serializers

from favorites_app.models.favorites import Favorite
from favorites_app.models.planets import Planet
from favorites_app.models.movies import Movie

from favorites_app.serializers.favorites import FavoriteSerializer


class FavoriteCreateView(generics.CreateAPIView):
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        content_type = self.request.data.get('content_type')
        object_id = self.request.data.get('object_id')
        custom_name = self.request.data.get('custom_name')

        if content_type not in ['movie', 'planet']:
            raise serializers.ValidationError("Invalid content type. Allowed values: 'movie' or 'planet'.")

        # Check if the object with the given content_type and object_id exists
        if content_type == 'movie':
            try:
                movie = Movie.objects.get(pk=object_id)
                if Favorite.objects.filter(user_id=user_id, movie=movie).exists():
                    raise serializers.ValidationError("Favorite of the movie for this user already exists")
            except Movie.DoesNotExist:
                raise serializers.ValidationError("Movie with the given ID does not exist.")
            serializer.save(movie=movie, planet=None)  # Set movie as the related object
        else:
            try:
                planet = Planet.objects.get(pk=object_id)
                if Favorite.objects.filter(user_id=user_id, planet=planet).exists():
                    raise serializers.ValidationError("Favorite of the movie for this user already exists")
            except Planet.DoesNotExist:
                raise serializers.ValidationError("Planet with the given ID does not exist.")
            serializer.save(movie=None, planet=planet)  # Set planet as the related object


class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
