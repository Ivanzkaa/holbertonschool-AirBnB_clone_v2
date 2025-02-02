#!/usr/bin/python3
"""a flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """displaying a message"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displaying hbnb"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def text():
    """displaying c_text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is_cool"):
    """displaying a python text"""
    text = text.replace('_', ' ')
    return 'Python {}'. format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """displaying number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
