#!/usr/bin/env python3
"""
Get Hyper Method
"""

get_page = __import__('1-simple_pagination').get_page


def get_hyper(page: int = 1, page_size: int = 10) -> dict:
    """
    Arguments:
    page (int) --> pagination parameter / default value = 1
    page_size (int) --> pagination parameter / default value = 10
    """
    