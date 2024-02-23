#!/usr/bin/env python3
""" Hashing Password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashing Password Function """
    _bytes = password.encode('utf-8')
    slat = bcrypt.gensalt()
    hash = bcrypt.hashpw(_bytes, slat)
    return hash