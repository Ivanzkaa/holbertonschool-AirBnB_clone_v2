#!/usr/bin/python3
"""starting a web flask application that
get the states list"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(text):
    """Removing the current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """showing the list of the states"""
    state_list = storage.all('State')
    return render_template('7-states_list.html', states=state_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
