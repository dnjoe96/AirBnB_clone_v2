#!/usr/bin/python3
""" route file """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ view definition hello_hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ view definition of hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def whatisc(text):
    """ view definition of whatisc"""
    final_text = text.replace("_", " ")
    return "C {}".format(final_text)


@app.route('/python')
@app.route('/python/<text>')
def show(text="is cool"):
    """ view definition of python """
    final_text = text.replace("_", " ")
    return "Python {}".format(final_text)


@app.route('/number/<int:n>')
def number(n):
    """ view definition for number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ view definition for number_template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ view definition for number_odd_or_even """
    if n % 2 == 0:
        dtype = 'even'
    else:
        dtype = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, dtype=dtype)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
