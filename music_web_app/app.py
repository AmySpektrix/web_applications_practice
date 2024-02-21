import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return repository.all()

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    repository.create(title,release_year,artist_id)
    return "Album added successfully", 200
    
@app.route('/artists', methods = ['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_names = [x.name for x in repository.all()]
    return ", ".join(artist_names)

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_name = request.form['artist_name']
    genre = request.form['genre']
    repository.create(artist_name,genre)
    return "Artist added successfully", 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

