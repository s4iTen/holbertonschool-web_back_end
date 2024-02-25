#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class"""

    def __init__(self):
        return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the path is in the excluded_paths list
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        for i in excluded_paths:
            if path.startswith(i) or excluded_paths == '/api/v1/status/':
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header method """
        if request is None:
            return None
        if "Authorization" in request.headers:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method """
        return None
