from flask import Flask, jsonify
""" this is the flask app """
app = Flask(__name__)


@app.route("/")
def hello_world():
    """ this is the route hello message"""
    data = {"message": "Bienvenue"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
