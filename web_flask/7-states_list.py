#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def print_states_list():
    strict_slashes = False
    list_of_state = storage.all('State')
    return render_template('7-states_list.html', list_of_state=list_of_state)


@app.teardown_appcontext
def close_storage(self):
    storage.close()

if __name__ == "__main__":
    app.run()
