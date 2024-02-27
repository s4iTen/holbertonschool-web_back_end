#!/usr/bin/env python3
''' Hash password '''
import bcrypt


def hash_password(password: str) -> bytes:
    """
    this function takes argument password as string
    and returns bytes
    """
    passwd = password.encode('utf-8')
    crypt_pass = bcrypt.gensalt()
    return bcrypt.hashpw(passwd, crypt_pass)
