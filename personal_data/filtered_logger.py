#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Arguments:
    fields (list(str)) --> all fields to obfuscate
    redaction (str) --> what the fiield will be obfuscated by
    message (str) --> log time
    separator(str) --> character separating all log time fields
    """
    pattern = re.('[eggcellent]', message)
    print(pattern)
