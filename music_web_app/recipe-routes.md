
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

GET/albums


POST /albums
  title: string
  release_year: string
  artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /albums
#  Expected response (200 OK):
"""
No response
"""

# GET /albums
#  Expected response (200 OK):
"""
List of albums
"""

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /albums
  Expected response (200 OK):
  List of albums in Json format
"""
def test_get_albums(web_client):
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
POST /albums
  Parameters:
    title: Red
    release_year: 2012
    artist_id: 4
  Expected response (200 OK)
"""
def test_post_submit(web_client):
    response = web_client.post('/albums', data={'title': 'Red', 'release_year': 2012, 'artist_id' = 3})
    assert response.status_code == 200
    response = web_client.get('/albums')
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
        {'id':910,'title':'Red','release_year':2012, 'artist_id':4},        
    ]
```

