#!/usr/bin/env python3
""" Hashing Password """


import bcrypt

def hash_password(password: str) -> bytes:
    """ Hashing Password Function """
    _bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(_bytes, salt)
    return hashed_password