#!/usr/bin/env python3
""" BasicAuth class """
from api.v1.auth.auth import Auth
import base64
import re
from typing import TypeVar
from models.user import User




class BasicAuth(Auth):
    """ basicAuth class """
    def __init__(self):
        return

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header method """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """ decode_base64_authorization_header method """
        if base64_authorization_header is None:
            if base64_authorization_header == "":
                return None
        try:
            tem = base64.b64decode(base64_authorization_header).decode('utf-8')
            return tem
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """extract_user_credentials method"""

        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) != str):
            return None, None
        if (re.search(':', decoded_base64_authorization_header)):
            res = re.split(':', decoded_base64_authorization_header)
            return res[0], res[1]
        else:
            return None, None

def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials method"""

        if type(user_email) != str or user_email is None:
            return None
        if type(user_pwd) != str or user_pwd is None:
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        for u in user:
            if u.is_valid_password(user_pwd):
                return u
        return None