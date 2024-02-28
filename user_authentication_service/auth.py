#!/usr/bin/env python3
''' Hash password '''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    this function takes argument password as string
    and returns bytes
    """
    passwd = password.encode('utf-8')
    crypt_pass = bcrypt.gensalt()
    return bcrypt.hashpw(passwd, crypt_pass)


def _generate_uuid() -> str:
    '''
    generate uuid function that return
    string representation of the uuid
    '''
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        this function takes argument email as string
        and password as string
        and returns a boolean
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        this function takes argument email as string
        and returns a string
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        this function takes argument session_id as string
        and returns an instance
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        this function takes argument user_id as integer
        and returns None
        """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
            return None
        except NoResultFound:
            pass
