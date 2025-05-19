#!/usr/bin/env python3
import re


def filter_datum(fields: str, redaction: str, message: str, separator: str):
    """
    Arguments:
    fields (list(str)) --> all fields to obfuscate
    redaction (str) --> what the fiield will be obfuscated by
    message (str) --> log time
    separator(str) --> character separating all log time fields
    """
    re.sub(r"password", "xxx", message)