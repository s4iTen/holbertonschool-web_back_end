#!/usr/bin/env python3
"""this is the flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _default_selector

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class will configure available languages in the app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@app.route('/')
def index():
    """ GET /
    Return: 2-index.html
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
