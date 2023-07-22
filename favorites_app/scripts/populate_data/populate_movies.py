import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'favorite.settings')

import django
django.setup()

from favorites_app.scripts.populate_data.data_readers.movies_reader import MoviesReader

def populate_movies_data():
    movies_reader = MoviesReader()
    movies_data = movies_reader.get_data()
    movies_reader.save_to_db()


if __name__ == '__main__':
    populate_movies_data()