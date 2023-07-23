from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from favorites_app.models.planets import Planet
from favorites_app.serializers.planets import PlanetSerializer


class PlanetListView(generics.ListAPIView):
    """
    View to retrieve a list of Star Wars planets or search by name.
    """
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'favorites__custom_name']

