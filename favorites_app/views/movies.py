from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from favorites_app.models.movies import Movie
from favorites_app.serializers.movies import MovieSerializer


class MovieListView(generics.ListAPIView):
    """
    View to retrieve a list of Star Wars movies or search by title.
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'favorites__custom_name']

