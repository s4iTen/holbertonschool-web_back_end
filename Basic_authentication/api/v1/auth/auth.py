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
            if path.startswith(i):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
