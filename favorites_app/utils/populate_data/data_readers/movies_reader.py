from favorites_app.utils.populate_data.data_readers.swapi import SwapiReader

from favorites_app.serializers.movies import MovieSerializer
class MoviesReader(SwapiReader):

    def __init__(self):
        url_path = "/api/films/"
        num_of_pages = 6
        super().__init__(url_path, num_of_pages)
        self._serializer = MovieSerializer

    def get_data(self):
        result = super().get_data()
        result = [{("updated" if k == "edited" else k): v for k, v in movie.items()} for movie in result]
        self.set_result(result)
        return self.get_result()


