#!/usr/bin/python3
"""
Flask application
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    Index entry for route /
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Index entry for route /hbnb
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Index entry for route /hbnb
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
