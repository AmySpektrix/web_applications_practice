import os
from flask import Flask, request

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
    

@app.route('/listings', methods=['GET'])
def all():
    return f"Hello {name}!"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

