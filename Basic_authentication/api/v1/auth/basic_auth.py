#!/usr/bin/env python3
""" Basic Authentication Module """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth Class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extract Base 64 Authorization Header Function """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        
        return authorization_header
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ Decode Base 64 Authorization Header Function """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        
        return ("{}:{}".format(str, str))
