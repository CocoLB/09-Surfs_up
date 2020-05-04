from flask import Flask

# create a new Flask instance called app:
app = Flask(__name__)

# Create Flask Routes
# root = starting point
#@app.route('/')
#def hello_world():
#	return 'Hello world'

#skill drill & Google

@app.route("/")
def hey():
    return "hey"

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/world")
def world():
    return "Hello world!"

