#!/usr/bin/env python3
""" Auth Module """
from flask import request
from typing import List, TypeVar
from os import getenv


""" Defined Class Auth """


class Auth:
    """ Initialize Class Auth """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth method """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        if path[-1] != "/":  # if no trailing slash
            path = path + "/"
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header method """
        if request is None:
            return None
        elif 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User Method """
        return None

    def session_cookie(self, request=None):
        """ Session Cookie Method """
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME")
        cookie_value = request.cookies.get(session_name)
        return cookie_value
