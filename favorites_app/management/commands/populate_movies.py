from django.core.management.base import BaseCommand
from favorites_app.utils.populate_data.data_readers.movies_reader import MoviesReader

class Command(BaseCommand):
    help = 'Populate data from starwars API to the Movie Model'

    def handle(self, *args, **kwargs):
        movies_reader = MoviesReader()
        movies_data = movies_reader.get_data()
        movies_reader.save_to_db()