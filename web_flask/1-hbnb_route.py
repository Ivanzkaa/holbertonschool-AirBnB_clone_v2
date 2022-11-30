#!/usr/bin/python3
"""a flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """displaying hbnb"""
    return ('HBNB')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
