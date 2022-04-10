#!/usr/bin/python3
""" route file """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>")
def whatisc(text):
    final_text = text.replace("_", " ")
    return f"C {final_text}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
