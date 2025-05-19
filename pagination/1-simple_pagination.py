#!/usr/bin/env python3
"""
The code from the previous task will be put here
"""
def get_page(page: int = 1, page_size: int = 10):
    """
    Arguments:
    page (int) --> pagination parameter / default value = 1
    page_size (int) --> pagination parameter / default value = 10
    
    Methods:
    Verify both arguments are > 0 (assert)
    Find correct indexes to paginate the dataset
    
    Returns:
    The appropriate page of the dataset
    If input arguments are out of range, return empty list
    """