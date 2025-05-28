#!/usr/bin/env python3
""" Filtered Logger Module """
import re
from typing import List
import os
import mysql.connector


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Arguments:
    fields (list(str)) --> all fields to obfuscate
    redaction (str) --> what the fiield will be obfuscated by
    message (str) --> log time
    separator(str) --> character separating all log time fields
        
    Methods:
    Regex Expression:
    (password | date_of_birth) --> matches either
    [^;]+ --> match characters (one or more) except a semicolon
    r'\1=' --> ensures the = sign is kept during re.sub with REDACTION
        
    Returns:
    The result of the regex
    """
    pattern = r'(password|date_of_birth)=([^;]+)'
    filtered = re.sub(pattern, r'\1=' + redaction, message)
    return (filtered)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to holberton databse and returns a connector
    Methods:
    Get environment variables:
    --> username
    --> password
    --> host
    --> database

    Returns:
    An SQL Connector
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        username=username,
        password=password,
        host=host,
        database=database
    )
