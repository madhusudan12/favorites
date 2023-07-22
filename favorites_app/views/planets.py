from rest_framework import generics
from favorites_app.models.planets import Planet
from favorites_app.serializers.planets import PlanetSerializer


class PlanetListView(generics.ListAPIView):
    """
    View to retrieve a list of Star Wars planets or search by name.
    """
    serializer_class = PlanetSerializer

    def get_queryset(self):
        """
        Returns a queryset of planets filtered by name if 'name' query parameter is provided.
        """
        queryset = Planet.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
