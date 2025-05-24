#!/usr/bin/env python3
""" Auth Module """
from flask import request
from typing import List, TypeVar



""" Defined Class Auth """
class Auth:
    """ Initialize Class Auth """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth method """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method """
        return None
