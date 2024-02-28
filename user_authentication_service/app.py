#!/usr/bin/env python3
from flask import Flask, jsonify
from auth import Auth
from flask import request
""" this is the flask app """

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    """ this is the route hello message"""
    return jsonify({"message": "Bienvenue"}), 200

AUTH = Auth()

@app.route("/users", methods=["POST"])
def register():
    """ this is the route register message"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
