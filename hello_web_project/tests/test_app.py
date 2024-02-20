# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


"""
When I make a POST request to /sort-names 
And: I send one name as the body parameter text
Then: I should get a 200 response returning that name
"""
def test_single_name_return(web_client):
    response = web_client.post('/sort-names', data={'names':'Amy'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Amy'


"""
When I make a POST request to /sort-names
And: I send no names in the body parameter text
Then: I should get a 400 response asking me to provide some names
"""

def test_no_names_return_error(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide some names'

"""
When I make a POST request to /sort-names 
And: I send multiple name as the body parameter text
Then: I should get a 200 response and a comma separated list of names which have been alphabetized
"""
def test_single_name_return(web_client):
    response = web_client.post('/sort-names', data={'names':'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When I make a GET request to /names
Then: I should get a 200 response and a list of predefined names
"""
def test_add_no_new_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'

"""
When I make a GET request to /names
And: I add a query parameter /names?add=Eddie
Then I should get a 200 response and a list with the new name added
"""
def test_add_one_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

"""
When I make a GET request to /names
And: I add a query parameter /names?add=Eddie,Leo
Then I should get a 200 response and a list with the new name added
"""
def test_add_two_name(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'