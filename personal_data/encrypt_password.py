#!/usr/bin/env python3
""" Hashing Password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashing Password Function """
    _bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(_bytes, salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check Password """
    _bytes = password.encode('utf-8')
    return bcrypt.checkpw(_bytes, hashed_password)
