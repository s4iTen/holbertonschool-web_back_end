#!/usr/bin/env python3
""" Task 6: Use user locale """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Documentation for gettext"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    locale_from_url = request.args.get("locale")
    if locale_from_url is not None and locale_from_url in Config.LANGUAGES:
        return locale_from_url
    
    user = g.get('user')
    if user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    
    locale_from_header = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale_from_header is not None:
        return locale_from_header
    
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except (ValueError, TypeError, KeyError):
        return None


@app.before_request
def before_request():
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
