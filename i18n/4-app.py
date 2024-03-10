#!/usr/bin/env python3
""" Task 3: Parametrize templates """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class will configure available languages in the app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returning our html page """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ get locale """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def gettext(text):
    """Translate text to the currently selected locale."""
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")