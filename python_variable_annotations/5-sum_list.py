#!/usr/bin/env python3
"""
Type-annotated function that takes a list of floats and returns the sum
"""
from typing import List
import typing as A


def sum_list(input_list: List[float]) -> float:
    """
    Parameters:
    input_list (list(floats)) --> list of floats
    
    Method:
    Use the sum() function to retrieve
    the sum of the input_list

    Returns:
    The sum of the list as floats
    """
    return (sum(input_list))
