from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", "Test Release Year", 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == "Test Release Year"
    assert album.artist_id == 1


"""
We can format artists to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Album", "Test Release Year", 1)
    assert str(album) == "Album(1, Test Album, Test Release Year, 1)"

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Album", "Test Release Year", 1)
    album2 = Album(1, "Test Album", "Test Release Year", 1)
    assert album1 == album2