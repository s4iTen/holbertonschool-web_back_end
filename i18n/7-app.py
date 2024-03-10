#!/usr/bin/env python3
""" Task 6: Use user locale and timezone """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz  # Import pytz for time zone validation


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
    locale = request.args.get("locale")
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    try:
        user = get_user()
        if user and user['locale'] in Config.LANGUAGES:
            return user['locale']
        raise Exception
    except Exception:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    # Check timezone from URL parameters
    timezone_from_url = request.args.get("timezone")
    if timezone_from_url is not None and validate_timezone(timezone_from_url):
        return timezone_from_url
    
    # Check timezone from user settings
    user = g.get('user')
    if user and validate_timezone(user['timezone']):
        return user['timezone']
    
    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


def validate_timezone(timezone):
    try:
        pytz.timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


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
