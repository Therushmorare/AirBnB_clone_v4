#!/usr/bin/python3
""" Flask Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ SQLAlchemy Session """
    storage.close()


@app.route('/2-hbnb', strict_slashes=False)
def hbnb():
    """ App Route """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_arr = []

    for state in states:
        state_arr.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('2-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=state_arr,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    """App  Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
