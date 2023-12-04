'''
1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# Request:
GET /names?add= string representing a name 
# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

GET /add_name
# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

GET /add_name 
# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

def test_add_name(web_client):
response = web_client.get('/add_name')
assert response.status_code == 200
assert response.data.decode ("utf-8") == 'Julia, Alice, Karim, Eddie'