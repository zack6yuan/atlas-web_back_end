#!/usr/bin/env python3
""" Basic Authentication Module """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth Class
    """
    def __init__(self):
        """ Constructor for the class BasicAuth """
        pass
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        elif not instanceof(authorization_header, str):
            return None
        elif authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header
