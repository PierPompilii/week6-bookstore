# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


def test_get_wave(web_client):
    response = web_client.get('/wave?name=Bruno')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'I am waving at Bruno'
    
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Bruno', 'message': 'Hello'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Thanks Bruno, you sent this message:Hello'
    
    
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode ("utf-8") == 'There are 3 vowels in "eee"'
    
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode ("utf-8") == 'There are 5 vowels in "eunoia"'
    
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'
    
    
def test_post_sort_names (web_client):
    response = web_client.post('/sort_names', data={'names':'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

def test_add_name(web_client):
    response = web_client.get('/add_name?name=Eddie')
    assert response.status_code == 200
    assert response.data.decode ("utf-8") == 'Julia, Alice, Karim, Eddie'