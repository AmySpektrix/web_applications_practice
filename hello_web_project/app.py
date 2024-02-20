import os
from flask import Flask, request
from lib.functions_for_app import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/', methods=['GET'])
def index():
    return "Blank index"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    goodbye = request.form['goodbye']
    return f"{goodbye} {name}!"

@app.route('/submit', methods=['POST'])
def submit_message():
    name = request.form['name']
    message = request.form ['message']
    return f"Thanks {name}, you sent this message: {message}"

@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']
    return f'There are {count_vowels_func(text)} vowels in "{text}"'

@app.route('/sort-names', methods = ['POST'])
def sort_names():
    if 'names' not in request.form:
        return 'Please provide some names', 400
    else:
        names = request.form['names']
        return alphabetize(names)

@app.route('/names', methods = ['GET'])
def names ():
    starting_names = 'Julia, Alice, Karim'
    if 'add' not in request.args:
        return starting_names
    else:
        add_param = request.args['add'] 
        return add_name_to_string(starting_names,add_param)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

