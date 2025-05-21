#!/usr/bin/env python3
""" Hash Password """
import bcrypt
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """
    Arguments:
    password (str) ---> user's password

    Methods:
    Encode the password to UTF-8 to pass to hashpw
    Generate a salt ---> data added to password before modification
    Pass the password to hashpw with the salt

    Returns:
    Salted, hashed password, which is a byte string
    """
    hashed_pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(hashed_pwd, salt)
    return hashed

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
        
    def register_user(email: str, password: str) -> User:
        if email instanceof(db):
            raise new ValueError("User {} already exists.".format(email))
        else:
            _hash_password(password, salt)
            
    def valid_login(email, password) -> bool:
         if (email):
             converted_pwd = password.encode('utf-8')
             check = bcrypt.checkpw(converted_pwd)
             """
             Implement the rest of the logic here
             """
             
    def _generate_uuid() -> str:
        """
        Generate UUIds
        
        Returns:
        String representation of a new UUID
        """
        new_identifier = uuid.uuid4()
        return str(new_identifier)
