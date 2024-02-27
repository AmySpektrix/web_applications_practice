from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)

    albums = album_repository.all()

    assert albums == [
        {'id':1,'title':'Doolittle','release_year':1989, 'artist_id':1},
        {'id':2,'title':'Surfer Rosa','release_year':1988, 'artist_id':1},
        {'id':3,'title':'Waterloo','release_year':1974, 'artist_id':2},
        {'id':4,'title':'Super Trouper','release_year':1980, 'artist_id':2},
        {'id':5,'title':'Bossanova','release_year':1990, 'artist_id':1},
        {'id':6,'title':'Lover','release_year':2019, 'artist_id':3},
        {'id':7,'title':'Folklore','release_year':2020, 'artist_id':3},
        {'id':8,'title':'I Put a Spell on You','release_year':1965, 'artist_id':4},                
        {'id':9,'title':'Baltimore','release_year':1978, 'artist_id':4},
    ]

"""
When we call AlbumRepository#find
With a particular id - it pulls the Album details for that particular ID
"""

def test_find_one_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)

    album_1 = album_repository.find(1)

    assert album_1 == Album(1,'Doolittle', 1989, 1)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Red (Taylor's Version)", 2021, 3)
    repository.create(album)
    assert album.id == 10
    albums = repository.all()
    assert albums == [
        {'id':1,'title':'Doolittle','release_year':1989, 'artist_id':1},
        {'id':2,'title':'Surfer Rosa','release_year':1988, 'artist_id':1},
        {'id':3,'title':'Waterloo','release_year':1974, 'artist_id':2},
        {'id':4,'title':'Super Trouper','release_year':1980, 'artist_id':2},
        {'id':5,'title':'Bossanova','release_year':1990, 'artist_id':1},
        {'id':6,'title':'Lover','release_year':2019, 'artist_id':3},
        {'id':7,'title':'Folklore','release_year':2020, 'artist_id':3},
        {'id':8,'title':'I Put a Spell on You','release_year':1965, 'artist_id':4},                
        {'id':9,'title':'Baltimore','release_year':1978, 'artist_id':4},
        {'id':10,'title':"Red (Taylor's Version)",'release_year':2021, 'artist_id':3},        
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3)

    albums = repository.all()
    assert albums == [
        {'id':1,'title':'Doolittle','release_year':1989, 'artist_id':1},
        {'id':2,'title':'Surfer Rosa','release_year':1988, 'artist_id':1},
        {'id':4,'title':'Super Trouper','release_year':1980, 'artist_id':2},
        {'id':5,'title':'Bossanova','release_year':1990, 'artist_id':1},
        {'id':6,'title':'Lover','release_year':2019, 'artist_id':3},
        {'id':7,'title':'Folklore','release_year':2020, 'artist_id':3},
        {'id':8,'title':'I Put a Spell on You','release_year':1965, 'artist_id':4},                
        {'id':9,'title':'Baltimore','release_year':1978, 'artist_id':4},
    ]
