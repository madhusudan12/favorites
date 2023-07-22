from django.core.management.base import BaseCommand
from favorites_app.utils.populate_data.data_readers.planet_reader import PlanetsReader

class Command(BaseCommand):
    help = 'Populate data from starwars API to the Planets Model'

    def handle(self, *args, **kwargs):
        planets_reader = PlanetsReader()
        planets_data = planets_reader.get_data()
        print(len(planets_data))
        planets_reader.save_to_db()