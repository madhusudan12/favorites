# Django Favorites App

The Django Favorites App is a simple web application that allows users to list and add their favorite Star Wars movies and planets. The app provides REST APIs for managing the movie and planet data, as well as APIs to add movies and planets to a user's favorites.

## Features

- List Star Wars movies and planets using the provided API from https://sw-api-rwjfuiltyq-el.a.run.app/.
- Expose list APIs for movies and planets.
- Expose APIs to add movies and planets as favorites.
- Support setting custom names for favorites.
- Favorites are stored per user (user_id can be passed in the request).
- List APIs return additional fields such as 'created', 'updated', 'URL', and 'is_favourite'.
- Support searching by title/name for both movies and planets.
- Use PostgreSQL as the database for data storage.
- Utilize Gunicorn as the WSGI server for deployment.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/django-favorites.git
cd django-favorites
```

1. Create and activate a virtual environment (optional but recommended):
```shell
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

2.Install the required dependencies:
```shell
pip install -r requirements.txt
```

3.Set up the PostgreSQL database:

 a.Create a new PostgreSQL database for the app.
 b.Add the database credentials (NAME, USER, PASSWORD, HOST, PORT) to the .env file in the project root. you can refer example .env.template
 
4.Apply migrations and create the database schema:
```shell
python manage.py migrate
```

5.Run the data population scripts to fetch movies and planets from the Star Wars API:
```shell
python manage.py populate_movies
python manage.py populate_planets
```

6. Start the Gunicorn server:
```shell
bash entrypoint.sh
```

The app is now running and accessible at http://localhost:8000/.

## API Endpoints

- **List Movies**: `/movies/`
  - Method: GET
  - Query Parameters: `title` (optional) - Filter movies by title.

- **List Planets**: `/planets/`
  - Method: GET
  - Query Parameters: `name` (optional) - Filter planets by name.

- **List Favorites**: `/favorites/`
  - Method: GET
  - Query Parameters: `user_id` (optional) - Filter favorites by user ID.

- **Add Favorite**: `/favorites/`
  - Method: POST
  - Request Body: JSON with the following fields:
    - `user_id`: Integer (required) - The user's ID.
    - `content_type`: String (required) - Either 'movie' or 'planet'.
    - `object_id`: UUID (required) - The ID of the movie or planet to be added as a favorite.
    - `custom_name`: String (optional) - Custom name for the favorite (if applicable).




## Testing
Test cases are not added yet
