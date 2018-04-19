#!/usr/bin/python3
"""
Flask initiated
"""
from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def numonly(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def template(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    dict = storage.all("State")
    states = dict.values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)