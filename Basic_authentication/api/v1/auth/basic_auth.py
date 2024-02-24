#!/usr/bin/env python3
""" BasicAuth class """
from api.v1.auth.auth import Auth
import base64


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
        """ extract_user_credentials method """
        if decoded_base64_authorization_header is None:
            return None, None
        if decoded_base64_authorization_header is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':', 1)
