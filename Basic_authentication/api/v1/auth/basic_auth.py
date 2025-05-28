#!/usr/bin/env python3
""" Basic Authentication Module """
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth Class """
    def extract_base64_authorization_header(
        self, authorization_header: str) -> str:
        """
        Extract Base 64 Authorization Header Function

        Methods:
        if authorization_header is None, not a string, or does not
        start with "Basic", return None
        Use string slicing to get the substring (After "Basic"
        and the space)

        Returns:
        The value after Basic, and the space
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        decoded = authorization_header[len("Basic "):]

        return decoded

    def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
        """ Decode Base 64 Authorization Header Function """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract User Credentials Function """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        return ("{}:{}".format(str, str))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ User Object From Credentials Function """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
