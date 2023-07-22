from favorites_app.utils.populate_data.data_readers.swapi import SwapiReader

from favorites_app.serializers.planets import PlanetSerializer

class PlanetsReader(SwapiReader):

    def __init__(self):
        url_path = "/api/planets/"
        num_of_pages = 60
        super().__init__(url_path, num_of_pages)
        self._serializer = PlanetSerializer

    def get_data(self):
        result = super().get_data()
        result = [{("updated" if k == "edited" else k): v for k, v in movie.items()} for movie in result]
        self.set_result(result)
        return self.get_result()

