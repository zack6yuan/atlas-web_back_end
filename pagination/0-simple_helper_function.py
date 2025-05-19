#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Arguments:
    page (int) --> pagination parameter
    page_size (int) --> pagination parameter
    
    Methods:
    Use start index and end index to handle pagination
    
    Returns:
    A tuple of the start and end indexes
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
