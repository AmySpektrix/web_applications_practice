from lib.artist import Artist

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["artist_name"], row["genre"])
            # the above connection causes each row to output as a dictionary with the header as the key and the value as the value
            artists.append(item)
        return artists

    # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["artist_name"], row["genre"])

    def find_id_from_name(self, artist_name):
        rows = self._connection.execute(
            'SELECT * from artists WHERE artist_name = %s', [artist_name])
        row = rows[0]
        return row["id"]

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        rows = self._connection.execute('INSERT INTO artists (artist_name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        row = rows[0]
        artist.id = row["id"]
        return artist

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None
