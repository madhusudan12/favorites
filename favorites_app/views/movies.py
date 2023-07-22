from rest_framework import generics
from favorites_app.models.movies import Movie
from favorites_app.serializers.movies import MovieSerializer


class MovieListView(generics.ListAPIView):
    """
    View to retrieve a list of Star Wars movies or search by title.
    """
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Returns a queryset of movies filtered by title if 'title' query parameter is provided.
        """
        queryset = Movie.objects.all()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
