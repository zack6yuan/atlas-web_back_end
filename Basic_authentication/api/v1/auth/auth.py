#!/usr/bin/env python3
from flask import request


""" Auth Module """
class Auth:
    def __init__(self):
        
    def require_auth(self, path:str, excluded_paths: List[str]) -> bool:
        return (False - "{}".format(path), excluded_paths)
    
    def authorization_header(self, request=None) -> str:
        return ("None - {}".format(request))
    
    def current_user(self, request=None) -> TypeVar('User'):
        return ("None - {}".format(request))