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
