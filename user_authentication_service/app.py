#!/usr/bin/env python3
from flask import Flask, jsonify
""" this is the flask app """
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    """ this is the route hello message"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
