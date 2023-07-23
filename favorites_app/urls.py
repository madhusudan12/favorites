from django.urls import path

from favorites_app.views.movies import MovieListView
from favorites_app.views.planets import PlanetListView
from favorites_app.views.favorites import FavoriteCreateView
from favorites_app.views.favorites import FavoriteListView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('planets/', PlanetListView.as_view(), name='planet-list'),
    path('favorites/', FavoriteCreateView.as_view(), name='favorite-create'),
    path('favorites/list/', FavoriteListView.as_view(), name='favorite-list'),
]
