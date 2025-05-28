#!/usr/bin/env python3
""" Auth Module """
import bcrypt
from db import DB
import uuid
from user import User
from sqlalchemy.orm.exc import NoResultFound


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

def _generate_uuid() -> str:
        """
        Generate UUIds
        
        Returns:
        String representation of a new UUID
        """
        new_identifier = uuid.uuid4()
        return str(new_identifier)

class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()
        
    """
    def register_user(self, email: str, password: str) -> User:
        if email and password:
            try:
                self._db.find_user_by(email=email)
            except NoResultFound:
                raise ValueError("User {} already exists".format(email))
    """
    

