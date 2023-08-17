#!/usr/bin/python3

"""
Task 0
"""

from flask import Flask, render_template
from flask import abort

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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text='is_cool'):
    """ Hello Python """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:number>", strict_slashes=False)
def hello_number(number):
    """ Hello number """
    return "{} is a number".format(number)


@app.route("/number_template/<int:number>", strict_slashes=False)
def number_template(number):
    """ Hello template """
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:number>", strict_slashes=False)
def odd_even_template(number):
    """ Odd or even template """
    if number % 2 != 0:
        return render_template("6-number_odd_or_even.html", number=number, text='odd')
    else:
        return render_template("6-number_odd_or_even.html", number=number, text='even')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
