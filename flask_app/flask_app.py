from flask import Flask

#This creates a new Flask object (application) named app
app = Flask(__name__)

#Routes(aka views) go here

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"





