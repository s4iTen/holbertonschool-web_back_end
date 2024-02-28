#!/usr/bin/env python3
''' Hash password '''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    this function takes argument password as string
    and returns bytes
    """
    passwd = password.encode('utf-8')
    crypt_pass = bcrypt.gensalt()
    return bcrypt.hashpw(passwd, crypt_pass)


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        this function takes argument email as string
        and password as string
        and returns an instance
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
