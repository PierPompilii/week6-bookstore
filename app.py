import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form ['message']
    return f'Thanks {name}, you sent this message:{message}' 

@app.route('/wave', methods=['GET'])
def post_wave():
    name = request.args['name']
    return f'I am waving at {name}'


@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form ['text']
    vowel = len([char for char in text if char in "aeiou"])
    return f'There are {vowel} vowels in "{text}"'

@app.route('/sort_names', methods=['POST'])
def post_sorted_names():
    names = request.form ['names'].split(',')
    sorte = sorted(names)
    return ','.join(sorte)
    
@app.route('/add_name', methods=['GET'])
def get_add_names():
    names = request.args ['name']
    return f'Julia, Alice, Karim, {names}'
    
    
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

