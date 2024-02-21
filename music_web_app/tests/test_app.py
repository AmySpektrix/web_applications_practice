# Tests for your routes go here
from lib.database_connection import *

"""
GET /albums
  Expected response (200 OK):
  List of albums in Json format
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/music_library_test_seed.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.json == [
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
when call POST /albums 
AND the body parameters are included below:
    title: Red
    release_year: 2012
    artist_id: 4
THEN I get a response of (200 OK) 
AND THEN when I call GET /albums the list reflects the new album
"""
def test_post_submit(db_connection, web_client):
    db_connection.seed('seeds/music_library_test_seed.sql')
    post_response = web_client.post('/albums', data={'title': 'Red', 'release_year': 2012, 'artist_id': 3})
    assert post_response.status_code == 200
    get_response = web_client.get('/albums')
    assert get_response.json == [
        {'id':1,'title':'Doolittle','release_year':1989, 'artist_id':1},
        {'id':2,'title':'Surfer Rosa','release_year':1988, 'artist_id':1},
        {'id':3,'title':'Waterloo','release_year':1974, 'artist_id':2},
        {'id':4,'title':'Super Trouper','release_year':1980, 'artist_id':2},
        {'id':5,'title':'Bossanova','release_year':1990, 'artist_id':1},
        {'id':6,'title':'Lover','release_year':2019, 'artist_id':3},
        {'id':7,'title':'Folklore','release_year':2020, 'artist_id':3},
        {'id':8,'title':'I Put a Spell on You','release_year':1965, 'artist_id':4},                
        {'id':9,'title':'Baltimore','release_year':1978, 'artist_id':4},
        {'id':10,'title':'Red','release_year':2012, 'artist_id':3},        
    ]

"""
When I call GET /artists
I receive a formatted list of artists from the database
"""
def test_get_artists_returns_list(db_connection, web_client):
    db_connection.seed('seeds/music_library_test_seed.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone'

"""
When I call POST /artists
AND I include body text specifying the name and genre
THEN I get a 200 response
AND THEN when I call Get /artists
THEN I see the new artist is added
"""
def test_add_new_artist(db_connection,web_client):
    db_connection.seed('seeds/music_library_test_seed.sql')
    post_response = web_client.post('artists', data={'artist_name':'Olafur Arnalds', 'genre':'modern classical'})
    assert post_response.status_code == 200
    get_response = web_client.get('/artists')
    assert get_response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone, Olafur Arnalds'