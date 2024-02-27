import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def find_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    return render_template("albums/album_id.html", album_title=album.title, release_year = album.release_year, artist_name = artist.name)

@app.route('/albums/new', methods=['GET'])
def new_album():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist_list= [artist.name for artist in artist_repo.all()]
    return render_template("albums/album_new.html", artist_list=artist_list)

@app.route('/albums/new', methods=['POST'])
def post_new_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repo = ArtistRepository(connection)
    title = request.form['album_title']
    release_year = request.form['release_year']
    artist_name = request.form['artist_name']
    artist_id = artist_repo.find_id_from_name(artist_name)
    album = Album(None,title,release_year,artist_id)
    repository.create(album)
    return redirect (f"/albums/{album.id}")
    


@app.route('/artists', methods = ['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/index.html", artists=artists)

@app.route('/artists/<int:id>', methods = ['GET'])
def get_one_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template("artists/artist.html", artist_name = artist.name, artist_id = artist.id, artist_genre = artist.genre)

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_name = request.form['artist_name']
    genre = request.form['genre']
    repository.create(artist_name,genre)
    return 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
