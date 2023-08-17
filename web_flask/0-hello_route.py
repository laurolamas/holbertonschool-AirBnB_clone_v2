#!/usr/bin/python3
"""
Task 0
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return "<p>Hello HBNB!</p>"
