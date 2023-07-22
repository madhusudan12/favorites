import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'favorite.settings')

import django
django.setup()

from favorites_app.scripts.populate_data.data_readers.planet_reader import PlanetsReader

def populate_planets_data():
    planets_reader = PlanetsReader()
    planets_data = planets_reader.get_data()
    planets_reader.save_to_db()


if __name__ == '__main__':
    populate_planets_data()