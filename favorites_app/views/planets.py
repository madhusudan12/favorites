from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from favorites_app.models.planets import Planet
from favorites_app.serializers.planets import PlanetSerializer


class PlanetListView(generics.ListAPIView):
    """
    View to retrieve a list of Star Wars planets or search by name.
    """
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'favorite__custom_name']

