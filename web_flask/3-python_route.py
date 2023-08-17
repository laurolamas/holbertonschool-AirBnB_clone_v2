#!/usr/bin/python3

"""
Task 0
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Hello world """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Hello HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """ Hello C """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
def hello_python(text='is_cool'):
    """ Hello Python """
    return "Pyhton {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
def hello_py():
    return "Python is cool"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
