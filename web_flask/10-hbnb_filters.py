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
    all_states = storage.all('State')
    all_amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=all_states,
    amenities=all_amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
