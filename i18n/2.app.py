#!/usr/bin/env python3
"""this is the flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.get('locale')
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/', strict_slashes=False)
def index():
    """index route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
