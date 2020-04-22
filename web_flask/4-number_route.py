#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<path:text>')
def c(text):
    strict_slashes = False
    new = text.replace("_", " ")
    return 'C %s' % new


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python(text):
    strict_slashes = False
    new = text.replace("_", " ")
    return 'Python %s' % new


@app.route('/number/<int:n>')
def number(n):
    strict_slashes = False
    return '%d is a number' % n

if __name__ == "__main__":
    app.run()
