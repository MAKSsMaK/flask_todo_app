from flask import Flask

app = Flask(__name__)

# Begining of smth cool
@app.route('/')
def hello_world():
    return '<p>Hello, world</p>'