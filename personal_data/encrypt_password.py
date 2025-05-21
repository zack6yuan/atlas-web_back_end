#!/usr/bin/env python3
"""
Encrypting Passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Arguments:
    hashed_password --> the previously hashed password
    password --> the new password from the user as input

    Methods:
    Convert the new password to utf-8 to pass to bcrypt
    Use checkpw to provided password to the hashed password

    Returns:
    The check for the password, as a Boolean (True or False)
    """
    converted_pwd = password.encode('utf-8')
    check = bcrypt.checkpw(converted_pwd, hashed_password)
    return check
